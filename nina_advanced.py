import os
import sys
import time
from datetime import datetime
from gpt4all import GPT4All

class NinaAdvanced:
    def __init__(self):
        print("🤖 Nina (version avancée) s'initialise...")
        
        # Configuration
        self.setup_directories()
        
        # État de l'assistant
        self.wake_word = "nina"
        self.conversation_history = []
        
        # Charger le modèle IA avancé
        self.load_advanced_model()
        
        print("✅ Nina (version avancée) est prête !")
        print("💡 Tapez 'nina' suivi de votre question")
        print("💡 Tapez 'nina stop' pour quitter")
        print("💡 Tapez 'aide' pour voir les commandes disponibles")
        print("🧠 Modèle IA avancé activé - conversations intelligentes disponibles !")
    
    def setup_directories(self):
        """Créer les dossiers nécessaires"""
        os.makedirs("logs", exist_ok=True)
        os.makedirs("models", exist_ok=True)
    
    def load_advanced_model(self):
        """Charger le modèle GPT4All avancé"""
        print("🧠 Chargement du modèle IA avancé...")
        try:
            # Utiliser Llama 3.2 3B - moderne et efficace
            print("📥 Téléchargement de Llama 3.2 3B (si première fois, peut prendre quelques minutes)...")
            self.gpt_model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf")
            print("✅ Modèle Llama 3.2 3B chargé avec succès !")
            print("🎯 Nina peut maintenant avoir des conversations vraiment intelligentes !")
            self.model_loaded = True
        except Exception as e:
            print(f"❌ Erreur lors du chargement du modèle: {e}")
            print("🔄 Passage en mode réponses simples...")
            self.gpt_model = None
            self.model_loaded = False
    
    def process_command(self, text):
        """Traiter la commande avec l'IA avancée"""
        if not text:
            return "Vous n'avez rien écrit. Essayez de poser une question !"
        
        # Utiliser le modèle avancé si disponible
        if self.model_loaded and self.gpt_model:
            return self.advanced_ai_response(text)
        else:
            return self.simple_responses(text)
    
    def advanced_ai_response(self, text):
        """Générer une réponse avec l'IA avancée"""
        try:
            # Préparer le contexte pour Nina comme Jarvis
            system_prompt = """Tu es Nina, un assistant IA vocal français inspiré de Jarvis d'Iron Man. 

Ton rôle :
- Être utile, intelligent et légèrement sophistiqué comme Jarvis
- Répondre en français de manière naturelle et concise
- Aider avec les questions, calculs, conseils, informations
- Garder un ton professionnel mais amical
- Être créatif et informatif selon les demandes

Instructions :
- Réponds toujours en français
- Sois précis et utile
- Adapte ton ton selon le contexte
- N'hésite pas à poser des questions de clarification si besoin"""

            # Ajouter l'historique récent pour la continuité
            if self.conversation_history:
                context_history = "\n".join(self.conversation_history[-3:])
                full_prompt = f"{system_prompt}\n\nHistorique récent:\n{context_history}\n\nUtilisateur: {text}\nNina:"
            else:
                full_prompt = f"{system_prompt}\n\nUtilisateur: {text}\nNina:"
            
            # Générer la réponse
            with self.gpt_model.chat_session():
                response = self.gpt_model.generate(full_prompt, max_tokens=300, temp=0.7)
            
            # Nettoyer la réponse
            response = response.strip()
            
            # Enlever les préfixes inutiles
            prefixes_to_remove = ["Nina:", "Assistant:", "IA:", "Réponse:"]
            for prefix in prefixes_to_remove:
                if response.startswith(prefix):
                    response = response[len(prefix):].strip()
            
            # S'assurer qu'on a une réponse valide
            if not response or len(response) < 3:
                return "Je n'ai pas bien compris votre demande. Pouvez-vous reformuler ?"
            
            return response
            
        except Exception as e:
            print(f"❌ Erreur avec l'IA avancée: {e}")
            return self.simple_responses(text)
    
    def simple_responses(self, text):
        """Réponses simples de secours"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["bonjour", "salut", "hello"]):
            return "Bonjour ! Je suis Nina, votre assistant IA. Le modèle avancé n'a pas pu se charger, mais je reste à votre service !"
        
        elif "heure" in text_lower:
            return f"Il est actuellement {datetime.now().strftime('%H:%M:%S')} ⏰"
        
        elif "date" in text_lower:
            return f"Nous sommes le {datetime.now().strftime('%d/%m/%Y')} 📅"
        
        elif any(word in text_lower for word in ["qui es-tu", "présente-toi"]):
            return "Je suis Nina, assistant IA inspiré de Jarvis. Le modèle avancé n'a pas pu se charger, mais je peux toujours vous aider !"
        
        elif "aide" in text_lower:
            return self.show_help()
        
        else:
            return (f"J'ai reçu votre message : '{text}'\n"
                   f"Le modèle IA avancé n'a pas pu se charger. Réessayez plus tard ou vérifiez votre connexion internet.")
    
    def show_help(self):
        """Afficher l'aide"""
        if self.model_loaded:
            return (
                "🤖 AIDE - Nina (version avancée)\n"
                "════════════════════════════════════\n"
                "🧠 IA avancée activée - Conversations naturelles !\n\n"
                "Capacités :\n"
                "• 💬 Conversations intelligentes sur tous sujets\n"
                "• 🧮 Calculs complexes et mathématiques\n"
                "• 📚 Explications détaillées et pédagogiques\n"
                "• 💡 Conseils personnalisés et créatifs\n"
                "• 🎯 Résolution de problèmes\n"
                "• 📝 Rédaction et correction de textes\n"
                "• 🌍 Informations générales\n"
                "• 🤖 Assistance technique\n\n"
                "Commandes spéciales :\n"
                "• 'nina stop' - Arrêter\n"
                "• 'aide' - Cette aide\n\n"
                "💡 Vous pouvez me parler naturellement de tout !"
            )
        else:
            return (
                "🤖 AIDE - Nina (mode simple)\n"
                "═══════════════════════════════\n"
                "⚠️ Le modèle avancé n'a pas pu se charger\n\n"
                "Capacités limitées disponibles :\n"
                "• Salutations\n"
                "• Heure et date\n"
                "• Informations de base\n\n"
                "Pour activer l'IA avancée, vérifiez votre connexion internet."
            )
    
    def detect_wake_word(self, text):
        """Détecter le mot de réveil ou permettre conversation libre"""
        text_lower = text.lower()
        
        # Commandes spéciales sans wake word
        if text_lower in ["aide", "help", "stop", "quit", "exit"]:
            return True
            
        # Wake word classique
        return self.wake_word.lower() in text_lower
    
    def log_conversation(self, user_input, ai_response):
        """Enregistrer la conversation"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sauvegarder dans l'historique (version courte pour le contexte)
        self.conversation_history.append(f"User: {user_input[:50]}... | Nina: {ai_response[:50]}...")
        
        # Limiter l'historique
        if len(self.conversation_history) > 5:
            self.conversation_history.pop(0)
        
        # Enregistrer dans un fichier log détaillé
        try:
            with open("logs/conversation_advanced.log", "a", encoding="utf-8") as f:
                f.write(f"{timestamp} - USER: {user_input}\n")
                f.write(f"{timestamp} - NINA: {ai_response}\n")
                f.write("-" * 80 + "\n")
        except Exception as e:
            print(f"⚠️ Erreur de log: {e}")
    
    def run(self):
        """Boucle principale de conversation avancée"""
        print("\n" + "="*60)
        print("🚀 Nina (version avancée) est en fonctionnement !")
        if self.model_loaded:
            print("🧠 IA avancée activée - Conversations naturelles disponibles")
        else:
            print("⚠️  Mode simple - IA avancée non disponible")
        print("💬 Commencez à taper vos messages...")
        print("="*60 + "\n")
        
        conversation_count = 0
        
        while True:
            try:
                # Demander l'entrée utilisateur
                user_input = input("👤 Vous: ").strip()
                
                if not user_input:
                    continue
                
                # Commandes spéciales
                if user_input.lower() in ["stop", "quit", "exit", "nina stop"]:
                    if self.model_loaded:
                        response = "Au revoir ! Ce fut un plaisir de converser avec vous. À bientôt ! 👋"
                    else:
                        response = "Au revoir ! Nina s'arrête. À bientôt ! 👋"
                    print(f"🤖 Nina: {response}")
                    break
                
                if user_input.lower() in ["aide", "help"]:
                    response = self.show_help()
                    print(f"🤖 Nina:\n{response}")
                    continue
                
                # Vérifier le wake word ou permettre conversation libre
                if self.detect_wake_word(user_input) or conversation_count > 0:
                    # Traiter la commande avec l'IA avancée
                    response = self.process_command(user_input)
                    print(f"🤖 Nina: {response}")
                    
                    # Enregistrer la conversation
                    self.log_conversation(user_input, response)
                    
                    conversation_count += 1
                    
                    # Encouragements
                    if conversation_count == 1 and self.model_loaded:
                        print("\n💡 Parfait ! L'IA avancée est activée. Vous pouvez me parler naturellement.")
                        print("   (Plus besoin de dire 'nina' à chaque fois maintenant)\n")
                    elif conversation_count == 1:
                        print("\n⚠️  Mode simple actif. Pour l'IA avancée, vérifiez votre connexion.\n")
                else:
                    print("🤖 Nina: Dites 'nina' suivi de votre question pour commencer, ou tapez 'aide' pour voir les commandes.")
                
            except KeyboardInterrupt:
                print("\n👋 Nina s'arrête (Ctrl+C détecté). Au revoir !")
                break
            except Exception as e:
                print(f"❌ Erreur inattendue: {e}")
                continue

# Point d'entrée
if __name__ == "__main__":
    try:
        nina = NinaAdvanced()
        nina.run()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1) 