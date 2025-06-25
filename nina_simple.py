import os
import sys
import time
import subprocess
from datetime import datetime
import whisper
from gpt4all import GPT4All
import sounddevice as sd
import soundfile as sf
import numpy as np

class NinaSimple:
    def __init__(self):
        print("🤖 Nina Simple s'initialise...")
        
        # Configuration
        self.setup_directories()
        self.setup_audio()
        
        # État de l'assistant
        self.wake_word = "nina"
        self.conversation_history = []
        
        # Charger les modèles étape par étape
        self.load_models()
        
        print("✅ Nina Simple est prête ! Dites 'Nina' pour commencer.")
    
    def setup_directories(self):
        """Créer les dossiers nécessaires"""
        os.makedirs("temp_audio", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
        os.makedirs("models", exist_ok=True)
    
    def setup_audio(self):
        """Configuration audio"""
        self.sample_rate = 16000
        self.audio_duration = 3  # 3 secondes pour Windows
    
    def load_models(self):
        """Charger les modèles IA un par un"""
        print("🧠 Chargement de Whisper (reconnaissance vocale)...")
        try:
            self.whisper_model = whisper.load_model("base")
            print("✅ Whisper chargé avec succès")
        except Exception as e:
            print(f"❌ Erreur Whisper: {e}")
            return False
        
        print("🧠 Chargement de GPT4All (IA de conversation)...")
        try:
            # Vérifier si le modèle existe
            model_path = "./models/ggml-gpt4all-j-v1.3-groovy.bin"
            if not os.path.exists(model_path):
                print("⚠️  Modèle GPT4All non trouvé. Utilisation du mode texte uniquement.")
                self.gpt_model = None
            else:
                self.gpt_model = GPT4All("ggml-gpt4all-j-v1.3-groovy.bin", model_path="./models")
                print("✅ GPT4All chargé avec succès")
        except Exception as e:
            print(f"⚠️  GPT4All non disponible: {e}")
            self.gpt_model = None
        
        return True
    
    def record_audio(self, filename="temp_audio/input.wav", duration=None):
        """Enregistrer l'audio du microphone"""
        if duration is None:
            duration = self.audio_duration
            
        print("🎙️ Écoute en cours...")
        
        try:
            audio = sd.rec(int(duration * self.sample_rate), 
                          samplerate=self.sample_rate, 
                          channels=1, dtype='float64')
            sd.wait()
            sf.write(filename, audio, self.sample_rate)
            return filename
        except Exception as e:
            print(f"❌ Erreur d'enregistrement: {e}")
            return None
    
    def speech_to_text(self, audio_file):
        """Convertir l'audio en texte"""
        try:
            result = self.whisper_model.transcribe(audio_file)
            return result["text"].strip()
        except Exception as e:
            print(f"❌ Erreur de transcription: {e}")
            return ""
    
    def process_command(self, text):
        """Traiter la commande et générer une réponse"""
        if not text:
            return "Je n'ai pas bien entendu, pouvez-vous répéter ?"
        
        # Réponses simples intégrées si GPT4All n'est pas disponible
        if self.gpt_model is None:
            return self.simple_responses(text)
        
        # Utiliser GPT4All si disponible
        try:
            context = f"Tu es Nina, un assistant IA vocal français comme Jarvis. "
            context += f"Réponds de manière naturelle et utile en français. "
            context += f"Historique récent: {' '.join(self.conversation_history[-2:])}"
            
            prompt = f"{context}\n\nUtilisateur: {text}\nNina:"
            
            response = self.gpt_model.generate(prompt, max_tokens=100, temp=0.7)
            
            # Nettoyer la réponse
            response = response.strip()
            if response.startswith("Nina:"):
                response = response[5:].strip()
            
            return response
        except Exception as e:
            print(f"❌ Erreur de génération: {e}")
            return self.simple_responses(text)
    
    def simple_responses(self, text):
        """Réponses simples si GPT4All n'est pas disponible"""
        text_lower = text.lower()
        
        if "bonjour" in text_lower or "salut" in text_lower:
            return "Bonjour ! Je suis Nina, votre assistant IA. Comment puis-je vous aider ?"
        elif "heure" in text_lower:
            return f"Il est {datetime.now().strftime('%H:%M')}"
        elif "date" in text_lower:
            return f"Nous sommes le {datetime.now().strftime('%d/%m/%Y')}"
        elif "merci" in text_lower:
            return "De rien ! C'est un plaisir de vous aider."
        elif "au revoir" in text_lower or "bye" in text_lower:
            return "Au revoir ! À bientôt !"
        elif "qui es-tu" in text_lower or "qui êtes-vous" in text_lower:
            return "Je suis Nina, votre assistant IA vocal, comme Jarvis !"
        else:
            return f"Vous avez dit : '{text}'. Je suis en mode simple pour l'instant. Téléchargez le modèle GPT4All pour des conversations plus avancées !"
    
    def speak_text(self, text):
        """Faire 'parler' Nina avec la synthèse vocale Windows"""
        try:
            # Utiliser la synthèse vocale intégrée de Windows
            subprocess.run([
                "powershell", 
                "-Command", 
                f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
            ], check=True)
        except Exception as e:
            print(f"❌ Erreur de synthèse vocale: {e}")
            print(f"💬 Nina (texte): {text}")
    
    def detect_wake_word(self, text):
        """Détecter le mot de réveil"""
        return self.wake_word.lower() in text.lower()
    
    def log_conversation(self, user_input, ai_response):
        """Enregistrer la conversation"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sauvegarder dans l'historique
        self.conversation_history.append(f"User: {user_input[:30]} | Nina: {ai_response[:30]}")
        
        # Limiter l'historique
        if len(self.conversation_history) > 5:
            self.conversation_history.pop(0)
        
        # Enregistrer dans un fichier log
        try:
            with open("logs/conversation.log", "a", encoding="utf-8") as f:
                f.write(f"{timestamp} - User: {user_input}\n")
                f.write(f"{timestamp} - Nina: {ai_response}\n\n")
        except Exception as e:
            print(f"⚠️ Erreur de log: {e}")
    
    def run(self):
        """Boucle principale de l'assistant"""
        print("🚀 Nina Simple est en fonctionnement !")
        print("💡 Dites 'Nina' suivi de votre question")
        print("💡 Dites 'Nina arrêt' pour quitter")
        print("💡 Appuyez sur Ctrl+C pour arrêter")
        
        while True:
            try:
                # Enregistrer l'audio
                audio_file = self.record_audio()
                if not audio_file:
                    continue
                
                # Convertir en texte
                user_text = self.speech_to_text(audio_file)
                if not user_text:
                    continue
                
                print(f"🗨️ Vous: {user_text}")
                
                # Vérifier le mot de réveil
                if self.detect_wake_word(user_text):
                    # Vérifier si c'est un arrêt
                    if "arrêt" in user_text.lower() or "stop" in user_text.lower():
                        response = "Au revoir ! Nina s'arrête."
                        print(f"🤖 Nina: {response}")
                        self.speak_text(response)
                        break
                    
                    # Traiter la commande
                    response = self.process_command(user_text)
                    print(f"🤖 Nina: {response}")
                    
                    # Faire parler Nina
                    self.speak_text(response)
                    
                    # Enregistrer la conversation
                    self.log_conversation(user_text, response)
                
                # Petit délai pour éviter la surcharge
                time.sleep(0.5)
                
            except KeyboardInterrupt:
                print("\n👋 Nina s'arrête. À bientôt !")
                break
            except Exception as e:
                print(f"❌ Erreur inattendue: {e}")
                continue

# Point d'entrée
if __name__ == "__main__":
    try:
        # Vérifier les périphériques audio
        print("🔊 Périphériques audio disponibles:")
        print(sd.query_devices())
        print()
        
        nina = NinaSimple()
        nina.run()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1) 