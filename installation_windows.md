# 🪟 Installation Nina sur Windows (Natif)

## 1️⃣ Prérequis Windows

### Installer Python 3.10+
- Télécharger depuis https://python.org
- ✅ Cocher "Add Python to PATH" durant l'installation

### Installer Git
- Télécharger depuis https://git-scm.com
- Utiliser les paramètres par défaut

### Installer FFmpeg
```powershell
# Option 1: Avec Chocolatey
choco install ffmpeg

# Option 2: Téléchargement manuel
# 1. Aller sur https://ffmpeg.org/download.html
# 2. Télécharger la version Windows
# 3. Extraire et ajouter au PATH
```

## 2️⃣ Installation rapide

### Créer le dossier projet
```cmd
mkdir C:\nina_assistant
cd C:\nina_assistant
```

### Créer l'environnement virtuel
```cmd
python -m venv env
env\Scripts\activate
```

### Installer les dépendances
```cmd
pip install --upgrade pip
pip install git+https://github.com/openai/whisper.git
pip install gpt4all
pip install TTS
pip install sounddevice soundfile numpy scipy
pip install requests beautifulsoup4 wikipedia-api
pip install python-dotenv schedule
```

### Télécharger le modèle IA
```cmd
mkdir models
cd models
# Télécharger manuellement depuis: https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin
# Placer le fichier dans le dossier models/
cd ..
```

## 3️⃣ Créer nina.py (Version Windows)

```python
import os
import sys
import json
import time
import threading
from datetime import datetime
import whisper
from gpt4all import GPT4All
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
import numpy as np
import subprocess

class NinaAssistant:
    def __init__(self):
        print("🤖 Nina s'initialise... Veuillez patienter")
        
        # Configuration
        self.setup_directories()
        self.load_models()
        self.setup_audio()
        
        # État de l'assistant
        self.is_listening = False
        self.wake_word = "nina"
        self.conversation_history = []
        
        print("✅ Nina est prête ! Dites 'Nina' pour commencer.")
    
    def setup_directories(self):
        """Créer les dossiers nécessaires"""
        os.makedirs("temp_audio", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
    
    def load_models(self):
        """Charger tous les modèles IA"""
        print("🧠 Chargement des modèles IA...")
        
        # Reconnaissance vocale
        self.whisper_model = whisper.load_model("base")
        
        # Modèle de langage
        self.gpt_model = GPT4All("ggml-gpt4all-j-v1.3-groovy.bin", model_path="./models")
        
        # Synthèse vocale (modèle anglais pour Windows)
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
        
        print("✅ Modèles chargés avec succès")
    
    def setup_audio(self):
        """Configuration audio"""
        self.sample_rate = 16000
        self.audio_duration = 3  # Réduit pour Windows
    
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
            return "I didn't hear you clearly, can you repeat?"
        
        # Contexte en anglais pour le modèle
        context = f"You are Nina, a helpful AI assistant like Jarvis. "
        context += f"Respond naturally and helpfully. "
        context += f"Recent history: {' '.join(self.conversation_history[-3:])}"
        
        prompt = f"{context}\n\nUser: {text}\nNina:"
        
        try:
            response = self.gpt_model.generate(prompt, max_tokens=150, temp=0.7)
            
            # Nettoyer la réponse
            response = response.strip()
            if response.startswith("Nina:"):
                response = response[5:].strip()
            
            return response
        except Exception as e:
            print(f"❌ Erreur de génération: {e}")
            return "I'm experiencing technical difficulties, sorry."
    
    def text_to_speech(self, text, filename="temp_audio/response.wav"):
        """Convertir le texte en parole"""
        try:
            self.tts.tts_to_file(text=text[:200], file_path=filename)  # Limiter la longueur
            return filename
        except Exception as e:
            print(f"❌ Erreur de synthèse: {e}")
            return None
    
    def play_audio(self, filename):
        """Jouer un fichier audio sur Windows"""
        try:
            # Utiliser Windows Media Player ou alternative
            subprocess.run([
                "powershell", 
                f"(New-Object Media.SoundPlayer '{filename}').PlaySync()"
            ], check=True)
        except Exception as e:
            print(f"❌ Erreur de lecture: {e}")
    
    def detect_wake_word(self, text):
        """Détecter le mot de réveil"""
        return self.wake_word.lower() in text.lower()
    
    def log_conversation(self, user_input, ai_response):
        """Enregistrer la conversation"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sauvegarder dans l'historique
        self.conversation_history.append(f"User: {user_input[:50]} | Nina: {ai_response[:50]}")
        
        # Limiter l'historique
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)
    
    def run(self):
        """Boucle principale de l'assistant"""
        print("🚀 Nina is running!")
        print("💡 Say 'Nina' followed by your question")
        print("💡 Say 'Nina stop' to quit")
        
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
                
                print(f"🗨️ You: {user_text}")
                
                # Vérifier le mot de réveil
                if self.detect_wake_word(user_text):
                    # Vérifier si c'est un arrêt
                    if "stop" in user_text.lower() or "quit" in user_text.lower():
                        print("👋 Nina is stopping. Goodbye!")
                        break
                    
                    # Traiter la commande
                    response = self.process_command(user_text)
                    print(f"🤖 Nina: {response}")
                    
                    # Convertir en audio et jouer
                    audio_response = self.text_to_speech(response)
                    if audio_response:
                        self.play_audio(audio_response)
                    
                    # Enregistrer la conversation
                    self.log_conversation(user_text, response)
                
                # Petit délai pour éviter la surcharge
                time.sleep(0.5)
                
            except KeyboardInterrupt:
                print("\n👋 Nina is stopping. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                continue

# Point d'entrée
if __name__ == "__main__":
    try:
        nina = NinaAssistant()
        nina.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
```

## 4️⃣ Lancement

```cmd
# Activer l'environnement
env\Scripts\activate

# Lancer Nina
python nina.py
```

## 🔧 Dépannage Windows

### Problème de microphone :
```python
# Tester les périphériques audio
import sounddevice as sd
print(sd.query_devices())
```

### Problème TTS :
- Utiliser un modèle anglais d'abord
- Installer manuellement espeak : https://espeak.sourceforge.net/download.html

### Modèle GPT4All :
- Télécharger manuellement depuis : https://gpt4all.io/models/
- Placer dans le dossier `models/` 