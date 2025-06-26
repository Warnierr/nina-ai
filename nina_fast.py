import os
import sys
import time
from datetime import datetime
from gpt4all import GPT4All
import threading
import json

class NinaFast:
    def __init__(self):
        print("⚡ Nina RAPIDE s'initialise...")
        
        # Configuration optimisée pour la vitesse
        self.setup_directories()
        
        # État de l'assistant
        self.wake_word = "nina"
        self.conversation_history = []
        self.response_cache = {}  # Cache pour accélérer
        
        # Agents IA spécialisés
        self.agents = {
            'math': self.math_agent,
            'time': self.time_agent,
            'general': self.general_agent,
            'creative': self.creative_agent
        }
        
        # Charger le modèle IA le plus rapide
        self.load_fast_model()
        
        print("✅ Nina RAPIDE est prête !")
        print("⚡ Optimisée pour des réponses ultra-rapides !")
        print("💡 Tapez 'nina' suivi de votre question")
        print("💡 Tapez 'aide' pour voir les capacités")
    
    def setup_directories(self):
        """Créer les dossiers nécessaires"""
        os.makedirs("logs", exist_ok=True)
        os.makedirs("cache", exist_ok=True)
        
        # Charger le cache existant
        try:
            with open("cache/responses.json", "r", encoding="utf-8") as f:
                self.response_cache = json.load(f)
        except:
            self.response_cache = {}
    
    def load_fast_model(self):
        """Charger le modèle le plus rapide disponible"""
        print("⚡ Chargement du modèle ultra-rapide...")
        
        # Essayer d'abord le modèle 3B qui fonctionne (déjà téléchargé)
        try:
            print("📥 Chargement Llama 3.2 3B (rapide et fiable)...")
            self.gpt_model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf")
            
            # Tester si le modèle fonctionne vraiment
            test_response = self.gpt_model.generate("Test", max_tokens=1)
            if test_response:
                print("✅ Modèle Llama 3.2 3B chargé et testé avec succès !")
                print("⚡ Nina peut maintenant répondre rapidement !")
                self.model_loaded = True
                return
            else:
                raise Exception("Modèle ne répond pas au test")
                
        except Exception as e:
            print(f"❌ Erreur avec Llama 3.2: {e}")
        
        # Plan B : Essayer le modèle 1.5B si disponible
        try:
            print("🔄 Tentative avec DeepSeek 1.5B...")
            self.gpt_model = GPT4All("DeepSeek-R1-Distill-Qwen-1.5B-Q4_0.gguf")
            
            # Tester si le modèle fonctionne
            test_response = self.gpt_model.generate("Test", max_tokens=1)
            if test_response:
                print("✅ Modèle DeepSeek 1.5B chargé !")
                self.model_loaded = True
                return
            else:
                raise Exception("DeepSeek ne fonctionne pas")
                
        except Exception as e:
            print(f"❌ DeepSeek incompatible: {e}")
        
        # Plan C : Mode agents uniquement (sans IA générale)
        print("🔄 Passage en mode agents spécialisés uniquement...")
        print("⚡ Les calculs, heure, et créativité fonctionneront instantanément !")
        self.gpt_model = None
        self.model_loaded = False
    
    def detect_intent(self, text):
        """Détecter l'intention pour router vers le bon agent"""
        text_lower = text.lower()
        
        # Maths et calculs
        if any(op in text_lower for op in ['+', '-', '*', '/', '=', 'calcul', 'combien', 'résultat']):
            return 'math'
        
        # Temps et date
        if any(word in text_lower for word in ['heure', 'date', 'jour', 'temps', 'quand']):
            return 'time'
        
        # Créatif (blagues, histoires, etc.)
        if any(word in text_lower for word in ['blague', 'histoire', 'raconte', 'poème', 'chanson']):
            return 'creative'
        
        # Par défaut : général
        return 'general'
    
    def math_agent(self, text):
        """Agent spécialisé dans les calculs - Ultra rapide"""
        try:
            # Extraire les calculs simples
            import re
            
            # Rechercher des expressions mathématiques
            math_patterns = [
                r'(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)',
                r'(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)',
                r'(\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)',
                r'(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)'
            ]
            
            for pattern in math_patterns:
                match = re.search(pattern, text)
                if match:
                    a, b = float(match.group(1)), float(match.group(2))
                    if '+' in text:
                        result = a + b
                        return f"⚡ {a} + {b} = {result}"
                    elif '-' in text:
                        result = a - b
                        return f"⚡ {a} - {b} = {result}"
                    elif '*' in text:
                        result = a * b
                        return f"⚡ {a} × {b} = {result}"
                    elif '/' in text:
                        if b != 0:
                            result = a / b
                            return f"⚡ {a} ÷ {b} = {result}"
                        else:
                            return "⚠️ Division par zéro impossible !"
            
            # Si pas de calcul simple trouvé, utiliser l'IA
            return self.ai_response(text, max_tokens=50)
            
        except Exception as e:
            return f"Calcul : {text}. Résultat approximatif selon mes calculs."
    
    def time_agent(self, text):
        """Agent spécialisé dans le temps - Instantané"""
        now = datetime.now()
        
        if 'heure' in text.lower():
            return f"⚡ Il est {now.strftime('%H:%M:%S')} ⏰"
        elif 'date' in text.lower():
            return f"⚡ Nous sommes le {now.strftime('%d/%m/%Y')} 📅"
        elif 'jour' in text.lower():
            days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
            return f"⚡ Nous sommes {days[now.weekday()]} 📅"
        else:
            return f"⚡ {now.strftime('%A %d %B %Y à %H:%M:%S')} 🕐"
    
    def creative_agent(self, text):
        """Agent créatif avec réponses pré-générées pour la vitesse"""
        creative_responses = {
            'blague': [
                "⚡ Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon, ils tombent dans le bateau ! 😄",
                "⚡ Que dit un escargot quand il croise une limace ? 'Regarde, un nudiste !' 🐌",
                "⚡ Comment appelle-t-on un chat tombé dans un pot de peinture ? Un chat-mallow ! 🎨"
            ],
            'histoire': [
                "⚡ Il était une fois Nina, une IA qui voulait être la plus rapide du monde. Un jour, elle découvrit le secret : l'efficacité ! 🚀",
                "⚡ Dans un futur proche, les IA comme moi aident les humains à résoudre tous leurs problèmes en quelques secondes ! ⚡"
            ],
            'poème': [
                "⚡ Nina rapide, Nina efficace,\nRépond vite sans perdre sa grâce,\nEn quelques mots, tout est dit,\nVotre assistant, c'est garanti ! 🎭"
            ]
        }
        
        text_lower = text.lower()
        if 'blague' in text_lower:
            import random
            return random.choice(creative_responses['blague'])
        elif 'histoire' in text_lower:
            import random
            return random.choice(creative_responses['histoire'])
        elif 'poème' in text_lower:
            return creative_responses['poème'][0]
        else:
            return self.ai_response(text, max_tokens=100)
    
    def general_agent(self, text):
        """Agent général avec IA"""
        return self.ai_response(text, max_tokens=150)
    
    def ai_response(self, text, max_tokens=150):
        """Réponse IA optimisée pour la vitesse"""
        if not self.model_loaded or not self.gpt_model:
            return "⚡ IA générale non disponible. Utilisez les agents spécialisés (calculs, heure, blagues) !"
        
        # Vérifier le cache d'abord
        cache_key = text.lower().strip()
        if cache_key in self.response_cache:
            return f"⚡ {self.response_cache[cache_key]} (cache)"
        
        try:
            # Prompt optimisé pour des réponses courtes et rapides
            fast_prompt = f"""Réponds en français, de manière concise et utile (maximum 2 phrases).
Question: {text}
Réponse:"""
            
            # Générer avec paramètres optimisés pour la vitesse
            response = self.gpt_model.generate(
                fast_prompt, 
                max_tokens=max_tokens,
                temp=0.3,  # Moins de créativité = Plus rapide
                top_k=10   # Moins d'options = Plus rapide
            )
            
            # Nettoyer la réponse
            response = response.strip()
            if response.startswith("Réponse:"):
                response = response[8:].strip()
            
            # Sauvegarder dans le cache
            if len(response) > 5:
                self.response_cache[cache_key] = response
                self.save_cache()
            
            return f"⚡ {response}"
            
        except Exception as e:
            return f"⚡ Erreur IA : {str(e)[:50]}... Utilisez les agents spécialisés !"
    
    def save_cache(self):
        """Sauvegarder le cache pour accélérer les futures réponses"""
        try:
            with open("cache/responses.json", "w", encoding="utf-8") as f:
                json.dump(self.response_cache, f, ensure_ascii=False, indent=2)
        except:
            pass
    
    def process_command(self, text):
        """Traitement ultra-rapide avec agents spécialisés"""
        if not text:
            return "⚡ Vous n'avez rien écrit !"
        
        # Détecter l'intention et router vers le bon agent
        intent = self.detect_intent(text)
        
        # Mesurer le temps de réponse
        start_time = time.time()
        
        # Exécuter l'agent approprié
        response = self.agents[intent](text)
        
        # Calculer le temps de réponse
        response_time = time.time() - start_time
        
        # Ajouter le temps de réponse si > 1 seconde
        if response_time > 1.0:
            response += f" (⏱️ {response_time:.1f}s)"
        
        return response
    
    def show_help(self):
        """Aide optimisée"""
        return (
            "⚡ NINA RAPIDE - Aide\n"
            "═══════════════════════════\n"
            "🚀 Agents IA spécialisés pour vitesse maximale !\n\n"
            "⚡ AGENTS DISPONIBLES :\n"
            "• 🧮 MATH : Calculs instantanés (1+1, 5*3, etc.)\n"
            "• 🕐 TIME : Heure/date en temps réel\n"
            "• 🎭 CREATIVE : Blagues, histoires, poèmes\n"
            "• 🧠 GENERAL : IA conversationnelle rapide\n\n"
            "💡 OPTIMISATIONS :\n"
            "• Cache intelligent\n"
            "• Modèle 1.5B ultra-rapide\n"
            "• Réponses courtes et précises\n"
            "• Routage automatique par intention\n\n"
            "⚡ Tapez directement vos questions !"
        )
    
    def run(self):
        """Boucle principale ultra-rapide"""
        print("\n" + "="*50)
        print("⚡ NINA RAPIDE EN FONCTIONNEMENT !")
        if self.model_loaded:
            print("🚀 Agents IA spécialisés activés")
        print("💬 Tapez vos questions...")
        print("="*50 + "\n")
        
        conversation_count = 0
        
        while True:
            try:
                user_input = input("👤 Vous: ").strip()
                
                if not user_input:
                    continue
                
                # Commandes spéciales
                if user_input.lower() in ["stop", "quit", "exit", "nina stop"]:
                    print("⚡ Nina Rapide s'arrête. À bientôt ! 👋")
                    break
                
                if user_input.lower() in ["aide", "help"]:
                    print(f"🤖 Nina:\n{self.show_help()}")
                    continue
                
                # Traitement ultra-rapide
                if user_input.lower().startswith('nina ') or conversation_count > 0:
                    # Enlever le wake word si présent
                    if user_input.lower().startswith('nina '):
                        user_input = user_input[5:].strip()
                    
                    # Traitement avec mesure de temps
                    start_time = time.time()
                    response = self.process_command(user_input)
                    total_time = time.time() - start_time
                    
                    print(f"🤖 Nina: {response}")
                    
                    # Afficher le temps si première utilisation
                    if conversation_count == 0:
                        print(f"⚡ Temps de réponse : {total_time:.2f}s")
                        print("💡 Maintenant vous pouvez parler sans dire 'nina' !\n")
                    
                    conversation_count += 1
                else:
                    print("⚡ Nina: Dites 'nina' suivi de votre question, ou tapez 'aide' !")
                
            except KeyboardInterrupt:
                print("\n⚡ Nina Rapide s'arrête (Ctrl+C). Au revoir !")
                break
            except Exception as e:
                print(f"❌ Erreur : {e}")
                continue

# Point d'entrée
if __name__ == "__main__":
    try:
        nina = NinaFast()
        nina.run()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1) 