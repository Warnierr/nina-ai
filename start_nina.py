#!/usr/bin/env python3
"""
LANCEUR NINA AI - SÉLECTEUR DE VERSION
=====================================
Script de lancement rapide pour choisir la bonne version de Nina
"""

import os
import sys
import subprocess
from datetime import datetime

class NinaLauncher:
    def __init__(self):
        self.versions = {
            '1': {
                'file': 'nina_fast.py',
                'name': 'Nina RAPIDE',
                'description': 'Version optimisée avec agents IA (RECOMMANDÉE)',
                'features': ['IA Llama 3.2 3B', 'Agents spécialisés', 'Cache intelligent', 'Ultra-rapide'],
                'usage': 'Usage quotidien, production'
            },
            '2': {
                'file': 'nina_advanced.py', 
                'name': 'Nina AVANCÉE',
                'description': 'IA conversationnelle avancée',
                'features': ['Llama 3.2 3B', 'Conversations intelligentes', 'Mode texte'],
                'usage': 'Conversations avancées, tests IA'
            },
            '3': {
                'file': 'nina_text.py',
                'name': 'Nina TEXTE',
                'description': 'Version simple et stable',
                'features': ['Mode texte pur', 'Très stable', 'Léger'],
                'usage': 'Tests rapides, développement'
            },
            '4': {
                'file': 'nina_simple.py',
                'name': 'Nina VOCALE',
                'description': 'Version originale avec reconnaissance vocale',
                'features': ['Reconnaissance vocale', 'Wake word "Nina"', 'Audio complet'],
                'usage': 'Tests audio, démonstrations vocales'
            },
            '5': {
                'file': 'nina_demo.py',
                'name': 'Nina DÉMO',
                'description': 'Démonstration complète avec 6 modules',
                'features': ['6 modules IA', 'Interface menu', 'Base de données', 'Démo auto'],
                'usage': 'Démonstrations, présentation'
            },
            '6': {
                'file': 'nina_test_interactive.py',
                'name': 'Nina TESTS',
                'description': 'Version de test et validation',
                'features': ['Tests automatiques', 'Menu interactif', 'Validation'],
                'usage': 'Tests, validation, développement'
            }
        }
    
    def show_welcome(self):
        """Affiche l'écran d'accueil"""
        print("=" * 60)
        print("🤖 LANCEUR NINA AI - SÉLECTEUR DE VERSION")
        print("=" * 60)
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🔧 Environnement: nina_env")
        print("✅ 6 versions fonctionnelles disponibles")
        print()
    
    def show_versions(self):
        """Affiche toutes les versions disponibles"""
        print("🚀 VERSIONS DISPONIBLES:")
        print("-" * 40)
        
        for key, version in self.versions.items():
            status = "🌟 RECOMMANDÉE" if key == '1' else "✅ Disponible"
            print(f"\n{key}. {version['name']} - {status}")
            print(f"   📝 {version['description']}")
            print(f"   🔧 Fonctionnalités: {', '.join(version['features'][:2])}...")
            print(f"   💡 Usage: {version['usage']}")
    
    def show_detailed_info(self, choice):
        """Affiche les informations détaillées d'une version"""
        if choice in self.versions:
            version = self.versions[choice]
            print(f"\n📋 INFORMATIONS DÉTAILLÉES - {version['name']}")
            print("-" * 50)
            print(f"📄 Fichier: {version['file']}")
            print(f"📝 Description: {version['description']}")
            print(f"💡 Usage: {version['usage']}")
            print(f"🔧 Fonctionnalités:")
            for feature in version['features']:
                print(f"   • {feature}")
            print()
    
    def launch_version(self, choice):
        """Lance la version sélectionnée"""
        if choice in self.versions:
            version = self.versions[choice]
            print(f"\n🚀 LANCEMENT DE {version['name']}...")
            print(f"📄 Fichier: {version['file']}")
            print("-" * 40)
            
            try:
                # Vérifier que le fichier existe
                if not os.path.exists(version['file']):
                    print(f"❌ Erreur: {version['file']} non trouvé!")
                    return False
                
                # Lancer la version
                subprocess.run([sys.executable, version['file']])
                return True
                
            except KeyboardInterrupt:
                print(f"\n⏹️  {version['name']} arrêtée par l'utilisateur")
                return True
            except Exception as e:
                print(f"❌ Erreur lors du lancement: {e}")
                return False
        else:
            print("❌ Version non valide!")
            return False
    
    def show_recommendations(self):
        """Affiche les recommandations d'usage"""
        print("\n💡 RECOMMANDATIONS D'USAGE:")
        print("-" * 30)
        print("🌟 Nouvel utilisateur → Nina RAPIDE (1)")
        print("🧠 IA avancée → Nina AVANCÉE (2)")
        print("⚡ Tests rapides → Nina TEXTE (3)")
        print("🎤 Audio/Vocal → Nina VOCALE (4)")
        print("🎯 Démonstration → Nina DÉMO (5)")
        print("🧪 Développement → Nina TESTS (6)")
    
    def run(self):
        """Boucle principale du lanceur"""
        self.show_welcome()
        
        while True:
            self.show_versions()
            self.show_recommendations()
            
            print(f"\n{'='*60}")
            print("ACTIONS DISPONIBLES:")
            print("• 1-6: Lancer une version")
            print("• 'info X': Informations détaillées (ex: info 1)")
            print("• 'test': Tester toutes les versions")
            print("• 'help': Aide complète")
            print("• 'quit': Quitter")
            
            choice = input(f"\n👤 Votre choix: ").strip().lower()
            
            if choice in ['quit', 'exit', 'q']:
                print("👋 Au revoir!")
                break
            
            elif choice in self.versions:
                self.show_detailed_info(choice)
                confirm = input("🚀 Lancer cette version ? (o/N): ").strip().lower()
                if confirm in ['o', 'oui', 'y', 'yes']:
                    self.launch_version(choice)
                    print(f"\n🔄 Retour au menu principal...")
            
            elif choice.startswith('info '):
                info_choice = choice.split()[1]
                if info_choice in self.versions:
                    self.show_detailed_info(info_choice)
                else:
                    print("❌ Version non valide pour info!")
            
            elif choice == 'test':
                print("\n🧪 LANCEMENT DES TESTS AUTOMATIQUES...")
                try:
                    subprocess.run([sys.executable, 'test_all_nina.py'])
                except Exception as e:
                    print(f"❌ Erreur tests: {e}")
            
            elif choice == 'help':
                self.show_help()
            
            else:
                print("❌ Choix non valide! Utilisez 1-6, info X, test, help ou quit")
            
            input("\n⏸️  Appuyez sur Entrée pour continuer...")
            print("\n" + "="*60)
    
    def show_help(self):
        """Affiche l'aide complète"""
        print("\n📖 AIDE COMPLÈTE DU LANCEUR NINA AI")
        print("=" * 40)
        print("""
🎯 OBJECTIF:
Ce lanceur vous aide à choisir et démarrer la bonne version de Nina AI
selon vos besoins spécifiques.

🔧 COMMANDES:
• 1-6        → Sélectionner et lancer une version
• info X     → Voir les détails de la version X
• test       → Tester toutes les versions
• help       → Cette aide
• quit       → Quitter le lanceur

💡 CONSEILS:
• Première utilisation → Choisissez Nina RAPIDE (1)
• Pour l'audio → Choisissez Nina VOCALE (4)  
• Pour des tests → Choisissez Nina TEXTE (3)
• Pour des démos → Choisissez Nina DÉMO (5)

🔍 INFORMATIONS TECHNIQUES:
• Toutes les versions sont testées et fonctionnelles
• L'environnement nina_env doit être activé
• Les modèles IA sont téléchargés automatiquement
        """)


def main():
    """Fonction principale"""
    try:
        launcher = NinaLauncher()
        launcher.run()
    except KeyboardInterrupt:
        print("\n👋 Lanceur arrêté. Au revoir!")
    except Exception as e:
        print(f"❌ Erreur fatale du lanceur: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 