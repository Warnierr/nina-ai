#!/usr/bin/env python3
"""
TEST AUTOMATIQUE DE TOUTES LES VERSIONS NINA
============================================
Teste et valide toutes les versions Nina fonctionnelles
"""

import os
import sys
import importlib
import subprocess
from datetime import datetime

class NinaTester:
    def __init__(self):
        self.results = {}
        self.working_versions = []
        self.broken_versions = []
        
    def test_import(self, module_name):
        """Teste l'importation d'un module"""
        try:
            importlib.import_module(module_name.replace('.py', ''))
            return True, "Import OK"
        except Exception as e:
            return False, str(e)
    
    def test_syntax(self, filename):
        """Teste la syntaxe d'un fichier Python"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                compile(f.read(), filename, 'exec')
            return True, "Syntaxe OK"
        except Exception as e:
            return False, str(e)
    
    def test_all_versions(self):
        """Teste toutes les versions Nina"""
        print("🧪 TEST AUTOMATIQUE DE TOUTES LES VERSIONS NINA")
        print("=" * 50)
        
        # Liste des fichiers Nina à tester
        nina_files = [
            'nina_simple.py',
            'nina_text.py', 
            'nina_advanced.py',
            'nina_fast.py',
            'nina_test_interactive.py',
            'nina_demo.py'
        ]
        
        for filename in nina_files:
            if os.path.exists(filename):
                print(f"\n🔍 Test de {filename}...")
                
                # Test syntaxe
                syntax_ok, syntax_msg = self.test_syntax(filename)
                
                # Test import
                import_ok, import_msg = self.test_import(filename)
                
                # Résultat
                if syntax_ok and import_ok:
                    status = "✅ FONCTIONNEL"
                    self.working_versions.append(filename)
                else:
                    status = "❌ DÉFAILLANT"
                    self.broken_versions.append(filename)
                
                print(f"   Syntaxe: {'✅' if syntax_ok else '❌'} {syntax_msg}")
                print(f"   Import:  {'✅' if import_ok else '❌'} {import_msg}")
                print(f"   Status:  {status}")
                
                self.results[filename] = {
                    'syntax': syntax_ok,
                    'import': import_ok,
                    'working': syntax_ok and import_ok
                }
            else:
                print(f"⚠️  {filename} non trouvé")
    
    def show_summary(self):
        """Affiche le résumé des tests"""
        print("\n" + "=" * 50)
        print("📊 RÉSUMÉ DES TESTS")
        print("=" * 50)
        
        print(f"\n✅ VERSIONS FONCTIONNELLES ({len(self.working_versions)}):")
        for version in self.working_versions:
            print(f"   • {version}")
        
        if self.broken_versions:
            print(f"\n❌ VERSIONS DÉFAILLANTES ({len(self.broken_versions)}):")
            for version in self.broken_versions:
                print(f"   • {version}")
        
        print(f"\n📈 STATISTIQUES:")
        total = len(self.results)
        working = len(self.working_versions)
        print(f"   • Total testé: {total}")
        print(f"   • Fonctionnel: {working}")
        print(f"   • Taux de succès: {(working/total*100):.1f}%" if total > 0 else "   • Aucun test")
    
    def generate_report(self):
        """Génère un rapport détaillé"""
        report_file = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("RAPPORT DE TEST NINA - VERSIONS FONCTIONNELLES\n")
            f.write("=" * 50 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("VERSIONS FONCTIONNELLES:\n")
            f.write("-" * 25 + "\n")
            for version in self.working_versions:
                f.write(f"✅ {version}\n")
            
            if self.broken_versions:
                f.write("\nVERSIONS DÉFAILLANTES:\n")
                f.write("-" * 22 + "\n")
                for version in self.broken_versions:
                    f.write(f"❌ {version}\n")
            
            f.write(f"\nSTATISTIQUES:\n")
            f.write("-" * 13 + "\n")
            total = len(self.results)
            working = len(self.working_versions)
            f.write(f"Total testé: {total}\n")
            f.write(f"Fonctionnel: {working}\n")
            f.write(f"Taux de succès: {(working/total*100):.1f}%\n" if total > 0 else "Aucun test\n")
        
        print(f"\n📄 Rapport sauvegardé: {report_file}")
    
    def recommend_versions(self):
        """Recommande les meilleures versions"""
        print("\n" + "=" * 50)
        print("🎯 RECOMMANDATIONS D'UTILISATION")
        print("=" * 50)
        
        recommendations = {
            'nina_simple.py': 'Version de base avec reconnaissance vocale',
            'nina_text.py': 'Version texte simple et fiable',
            'nina_advanced.py': 'Version avancée avec Llama 3.2 3B',
            'nina_fast.py': 'Version optimisée avec agents IA',
            'nina_test_interactive.py': 'Version de test et validation',
            'nina_demo.py': 'Version démo complète et stable'
        }
        
        print("\n🌟 VERSIONS RECOMMANDÉES:")
        for version in self.working_versions:
            if version in recommendations:
                print(f"   • {version}")
                print(f"     → {recommendations[version]}")
        
        # Recommandations spécifiques
        print("\n💡 CONSEILS D'UTILISATION:")
        if 'nina_fast.py' in self.working_versions:
            print("   🚀 Pour usage quotidien: nina_fast.py")
        if 'nina_text.py' in self.working_versions:
            print("   📝 Pour tests rapides: nina_text.py")
        if 'nina_advanced.py' in self.working_versions:
            print("   🧠 Pour IA avancée: nina_advanced.py")
        if 'nina_demo.py' in self.working_versions:
            print("   🎯 Pour démonstration: nina_demo.py")


def main():
    """Fonction principale"""
    try:
        tester = NinaTester()
        tester.test_all_versions()
        tester.show_summary()
        tester.generate_report()
        tester.recommend_versions()
        
        print(f"\n🏆 Tests terminés avec succès!")
        print(f"   {len(tester.working_versions)} versions fonctionnelles identifiées")
        
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 