import os
import sys
import time
from datetime import datetime
from gpt4all import GPT4All

class NinaText:
    def __init__(self):
        print("🤖 Nina (mode texte) s'initialise...")
        
        # Configuration
        self.setup_directories()
        
        # État de l'assistant
        self.wake_word = "nina"
        self.conversation_history = []
        
        # Charger le modèle IA
        self.load_model()
        
        print("✅ Nina (mode texte) est prête !")
        print("💡 Tapez 'nina' suivi de votre question")
        print("💡 Tapez 'nina stop' pour quitter")
        print("💡 Tapez 'aide' pour voir les commandes disponibles")
    
    def setup_directories(self):
        """Créer les dossiers nécessaires"""
        os.makedirs("logs", exist_ok=True)
        os.makedirs("models", exist_ok=True)
    
    def load_model(self):
        """Charger le modèle GPT4All"""
        print("🧠 Chargement du modèle IA...")
        try:
            # Vérifier si le modèle existe
            model_path = "./models/ggml-gpt4all-j-v1.3-groovy.bin"
            if not os.path.exists(model_path):
                print("⚠️  Modèle GPT4All non trouvé.")
                print("📥 Pour télécharger le modèle (optionnel) :")
                print("   1. Créez le dossier 'models'")
                print("   2. Téléchargez depuis : https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin")
                print("   3. Placez le fichier dans ./models/")
                print("")
                print("🔄 Utilisation du mode réponses simples pour l'instant...")
                self.gpt_model = None
            else:
                self.gpt_model = GPT4All("ggml-gpt4all-j-v1.3-groovy.bin", model_path="./models")
                print("✅ Modèle GPT4All chargé avec succès")
        except Exception as e:
            print(f"⚠️  Erreur lors du chargement du modèle: {e}")
            print("🔄 Utilisation du mode réponses simples...")
            self.gpt_model = None
    
    def process_command(self, text):
        """Traiter la commande et générer une réponse"""
        if not text:
            return "Vous n'avez rien écrit. Essayez de poser une question !"
        
        # Réponses simples si GPT4All n'est pas disponible
        if self.gpt_model is None:
            return self.simple_responses(text)
        
        # Utiliser GPT4All si disponible
        try:
            context = f"Tu es Nina, un assistant IA français comme Jarvis. "
            context += f"Réponds de manière naturelle, utile et concise en français. "
            context += f"Tu peux aider avec des questions générales, des calculs, des conseils, etc. "
            
            if self.conversation_history:
                context += f"Historique récent: {' '.join(self.conversation_history[-2:])}"
            
            prompt = f"{context}\n\nUtilisateur: {text}\nNina:"
            
            response = self.gpt_model.generate(prompt, max_tokens=200, temp=0.7)
            
            # Nettoyer la réponse
            response = response.strip()
            if response.startswith("Nina:"):
                response = response[5:].strip()
            
            return response
        except Exception as e:
            print(f"❌ Erreur avec le modèle IA: {e}")
            return self.simple_responses(text)
    
    def simple_responses(self, text):
        """Réponses simples mais intelligentes si GPT4All n'est pas disponible"""
        text_lower = text.lower()
        
        # Salutations
        if any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir", "bonne nuit"]):
            import random
            salutations = [
                "Bonjour ! Je suis Nina, votre assistant IA. Comment puis-je vous aider aujourd'hui ?",
                "Salut ! Ravi de vous parler ! Que puis-je faire pour vous ?",
                "Hello ! Nina à votre service. Qu'est-ce qui vous amène ?",
                "Bonjour ! J'espère que vous passez une bonne journée. Comment puis-je vous assister ?"
            ]
            return random.choice(salutations)
        
        # Heure et date
        elif "heure" in text_lower:
            return f"Il est actuellement {datetime.now().strftime('%H:%M:%S')} ⏰"
        elif "date" in text_lower:
            from datetime import datetime
            date_str = datetime.now().strftime('%A %d %B %Y')
            return f"Nous sommes {date_str} 📅"
        
        # Informations sur Nina
        elif any(word in text_lower for word in ["qui es-tu", "qui êtes-vous", "présente-toi", "qui tu es"]):
            return ("Je suis Nina, votre assistant IA vocal inspiré de Jarvis ! 🤖\n"
                   "En mode texte pour l'instant, mais je peux déjà :\n"
                   "• Répondre à vos questions\n"
                   "• Faire des calculs\n"
                   "• Donner des conseils\n"
                   "• Raconter des blagues\n"
                   "• Et bien plus encore !")
        
        # Calculs mathématiques
        elif any(op in text_lower for op in ["calcul", "calculate", "combien", "+", "-", "*", "/", "plus", "moins", "fois", "multiplié", "divisé"]):
            return self.handle_math(text)
        
        # Blagues
        elif any(word in text_lower for word in ["blague", "joke", "rigole", "drôle", "marrant"]):
            import random
            blagues = [
                "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon, ils tombent dans le bateau ! 😄",
                "Que dit un escargot quand il croise une limace ? 'Regarde ce nudiste !' 🐌",
                "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël ? Un chat-mallow ! 🎨",
                "Que dit un informaticien quand il s'ennuie ? Je me cache ! (cache = mémoire cache) 💻",
                "Pourquoi les poissons n'aiment pas jouer au tennis ? Parce qu'ils ont peur du filet ! 🐟"
            ]
            return random.choice(blagues)
        
        # Conseils
        elif any(word in text_lower for word in ["conseil", "aide-moi", "comment", "astuce", "tip"]):
            if "productif" in text_lower or "travail" in text_lower:
                return ("💡 Conseils pour être plus productif :\n"
                       "• Technique Pomodoro : 25min travail + 5min pause\n"
                       "• Éliminez les distractions (notifications, réseaux sociaux)\n"
                       "• Priorisez 3 tâches importantes par jour\n"
                       "• Prenez des vraies pauses pour recharger votre cerveau\n"
                       "• Dormez 7-8h par nuit pour être au top !")
            elif "sommeil" in text_lower or "dormir" in text_lower:
                return ("😴 Conseils pour bien dormir :\n"
                       "• Pas d'écrans 1h avant le coucher\n"
                       "• Température fraîche dans la chambre (18-20°C)\n"
                       "• Routine relaxante le soir\n"
                       "• Évitez la caféine après 14h\n"
                       "• Couchez-vous à heures régulières")
            else:
                return "Je serais ravi de vous donner des conseils ! Sur quel sujet avez-vous besoin d'aide ? (travail, sommeil, santé, etc.)"
        
        # Émotions et sentiments
        elif any(word in text_lower for word in ["triste", "déprimé", "mal", "difficile", "problème"]):
            return ("Je comprends que vous traversez un moment difficile. 💙\n"
                   "Voici quelques suggestions :\n"
                   "• Parlez à quelqu'un de confiance\n"
                   "• Prenez l'air et bougez un peu\n"
                   "• Respirez profondément et lentement\n"
                   "• Rappelez-vous que les difficultés sont temporaires\n"
                   "Si ça persiste, n'hésitez pas à consulter un professionnel.")
        
        elif any(word in text_lower for word in ["content", "heureux", "joie", "génial", "super"]):
            return "C'est formidable ! 😊 Je suis ravi que vous alliez bien. Votre bonne humeur est contagieuse !"
        
        # Questions philosophiques
        elif "sens de la vie" in text_lower or "pourquoi vivre" in text_lower:
            return ("🤔 Grande question philosophique ! Voici quelques pistes :\n"
                   "• Créer des liens significatifs avec les autres\n"
                   "• Apprendre et grandir constamment\n"
                   "• Contribuer positivement au monde\n"
                   "• Trouver ce qui vous passionne\n"
                   "• Profiter des petits bonheurs quotidiens\n"
                   "Le sens de la vie est souvent ce que vous décidez d'en faire !")
        
        # Technologie et IA
        elif any(word in text_lower for word in ["intelligence artificielle", "ia", "robot", "futur", "technologie"]):
            return ("🤖 L'IA est fascinante ! Elle peut :\n"
                   "• Aider à résoudre des problèmes complexes\n"
                   "• Automatiser des tâches répétitives\n"
                   "• Augmenter nos capacités humaines\n"
                   "• Créer de nouvelles possibilités\n"
                   "L'important est de l'utiliser de manière éthique et bienveillante !")
        
        # Aide
        elif "aide" in text_lower:
            return self.show_help()
        
        # Remerciements
        elif any(word in text_lower for word in ["merci", "thank you", "thanks"]):
            import random
            remerciements = [
                "De rien ! C'est un plaisir de vous aider ! 😊",
                "Je vous en prie ! N'hésitez pas si vous avez d'autres questions !",
                "Avec plaisir ! C'est pour ça que je suis là !",
                "Tout le plaisir est pour moi ! 🤖"
            ]
            return random.choice(remerciements)
        
        # Au revoir
        elif any(word in text_lower for word in ["au revoir", "bye", "à bientôt", "salut"]):
            import random
            aurevoir = [
                "Au revoir ! J'espère avoir pu vous aider. À bientôt ! 👋",
                "À très bientôt ! Passez une excellente journée ! ☀️",
                "Bye ! N'hésitez pas à revenir quand vous voulez ! 😊",
                "À plus tard ! Prenez soin de vous ! 💙"
            ]
            return random.choice(aurevoir)
        
        # Capacités
        elif any(word in text_lower for word in ["capacité", "que peux-tu faire", "fonctions", "talents"]):
            return ("🤖 Mes capacités actuelles (mode simple) :\n"
                   "• ✅ Conversations naturelles\n"
                   "• ✅ Calculs mathématiques\n"
                   "• ✅ Blagues et divertissement\n"
                   "• ✅ Conseils pratiques\n"
                   "• ✅ Support émotionnel\n"
                   "• ✅ Informations générales\n"
                   "• ✅ Heure et date\n"
                   "\n💡 Avec GPT4All, je pourrais faire bien plus !")
        
        # Tests
        elif "test" in text_lower:
            return "Test réussi ! Nina fonctionne parfaitement en mode texte. 🎉 Que voulez-vous tester d'autre ?"
        
        # Météo (exemple)
        elif "météo" in text_lower or "temps" in text_lower:
            return ("🌤️ Je ne peux pas encore accéder aux données météo en temps réel, mais cette fonctionnalité peut être ajoutée !\n"
                   "En attendant, regardez par la fenêtre ou consultez votre app météo préférée ! 😊")
        
        # Bismillah (réponse culturellement appropriée)
        elif "bismillah" in text_lower:
            return "Bismillah ! Que la bénédiction soit avec vous. Comment puis-je vous aider aujourd'hui ? 🤲"
        
        # Questions créatives
        elif any(word in text_lower for word in ["créativité", "idée", "inspiration", "créatif"]):
            return ("💡 Pour stimuler votre créativité :\n"
                   "• Changez d'environnement de travail\n"
                   "• Essayez de nouvelles expériences\n"
                   "• Tenez un carnet d'idées\n"
                   "• Collaborez avec d'autres personnes\n"
                   "• Prenez des pauses créatives régulières")
        
        # Réponse intelligente par défaut
        else:
            # Analyser le contenu pour une réponse plus pertinente
            if "?" in text:
                return ("🤔 C'est une question intéressante ! En mode simple, mes réponses sont limitées, mais voici ma réflexion :\n"
                       f"À propos de '{text}', je pense qu'il serait utile d'explorer différents angles. "
                       f"Tapez 'aide' pour voir mes capacités actuelles, ou téléchargez GPT4All pour des conversations plus approfondies !")
            else:
                return (f"J'ai bien reçu votre message : '{text}' 📝\n"
                       f"En mode simple, je peux répondre aux salutations, calculs, blagues, conseils, etc.\n"
                       f"Tapez 'aide' pour voir tout ce que je peux faire, ou essayez 'nina raconte une blague' !")
    
    def handle_math(self, text):
        """Gérer les calculs mathématiques"""
        import re
        
        # Nettoyer le texte pour extraire l'expression mathématique
        text_clean = text.lower().replace("nina", "").replace("calcule", "").replace("combien fait", "").replace("combien", "").strip()
        
        # Remplacer les mots par des symboles
        text_clean = text_clean.replace("plus", "+").replace("moins", "-").replace("fois", "*").replace("multiplié par", "*").replace("divisé par", "/")
        
        # Chercher une expression mathématique
        math_pattern = r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)'
        match = re.search(math_pattern, text_clean)
        
        if match:
            try:
                num1 = float(match.group(1))
                operator = match.group(2)
                num2 = float(match.group(3))
                
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        return "❌ Erreur : Division par zéro impossible !"
                
                # Formater le résultat
                if result.is_integer():
                    result = int(result)
                
                return f"🧮 {num1} {operator} {num2} = {result}"
                
            except:
                return "❌ Erreur dans le calcul. Essayez un format comme '25 + 17' ou '8 * 9'"
        else:
            return ("🧮 Je peux faire des calculs ! Essayez par exemple :\n"
                   "• 'nina calcule 25 + 17'\n"
                   "• 'combien fait 8 * 9'\n"
                   "• '15 - 3'\n"
                   "• '100 / 4'")
    
    def show_help(self):
        """Afficher l'aide"""
        return (
            "🤖 AIDE - Nina (mode texte)\n"
            "═══════════════════════════════\n"
            "Commandes disponibles :\n"
            "• 'nina [question]' - Poser une question\n"
            "• 'nina bonjour' - Me saluer\n"
            "• 'nina quelle heure' - Connaître l'heure\n"
            "• 'nina qui es-tu' - En savoir plus sur moi\n"
            "• 'nina test' - Vérifier que je fonctionne\n"
            "• 'nina aide' - Afficher cette aide\n"
            "• 'nina stop' - Me fermer\n"
            "\n"
            "Exemples de questions :\n"
            "• 'nina raconte-moi une blague'\n"
            "• 'nina quel est le sens de la vie'\n"
            "• 'nina conseils pour être productif'\n"
            "\n"
            "💡 Astuce: Pas besoin de toujours dire 'nina' au début !"
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
        
        # Sauvegarder dans l'historique (version courte)
        self.conversation_history.append(f"User: {user_input[:50]} | Nina: {ai_response[:50]}")
        
        # Limiter l'historique
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)
        
        # Enregistrer dans un fichier log
        try:
            with open("logs/conversation_text.log", "a", encoding="utf-8") as f:
                f.write(f"{timestamp} - USER: {user_input}\n")
                f.write(f"{timestamp} - NINA: {ai_response}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"⚠️ Erreur de log: {e}")
    
    def run(self):
        """Boucle principale de conversation"""
        print("\n" + "="*50)
        print("🚀 Nina (mode texte) est en fonctionnement !")
        print("💬 Commencez à taper vos messages...")
        print("="*50 + "\n")
        
        conversation_count = 0
        
        while True:
            try:
                # Demander l'entrée utilisateur
                user_input = input("👤 Vous: ").strip()
                
                if not user_input:
                    continue
                
                # Commandes spéciales
                if user_input.lower() in ["stop", "quit", "exit", "nina stop"]:
                    response = "Au revoir ! Nina s'arrête. À bientôt ! 👋"
                    print(f"🤖 Nina: {response}")
                    break
                
                if user_input.lower() in ["aide", "help"]:
                    response = self.show_help()
                    print(f"🤖 Nina:\n{response}")
                    continue
                
                # Vérifier le wake word ou permettre conversation libre
                if self.detect_wake_word(user_input) or conversation_count > 0:
                    # Traiter la commande
                    response = self.process_command(user_input)
                    print(f"🤖 Nina: {response}")
                    
                    # Enregistrer la conversation
                    self.log_conversation(user_input, response)
                    
                    conversation_count += 1
                    
                    # Encouragements
                    if conversation_count == 1:
                        print("\n💡 Parfait ! Vous pouvez continuer à poser des questions librement.")
                        print("   (Plus besoin de dire 'nina' à chaque fois maintenant)\n")
                else:
                    print("🤖 Nina: Dites 'nina' suivi de votre question pour commencer, ou tapez 'aide' pour voir les commandes.")
                
            except KeyboardInterrupt:
                print("\n👋 Nina s'arrête (Ctrl+C détecté). À bientôt !")
                break
            except Exception as e:
                print(f"❌ Erreur inattendue: {e}")
                continue

# Point d'entrée
if __name__ == "__main__":
    try:
        nina = NinaText()
        nina.run()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1) 