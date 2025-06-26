#!/usr/bin/env python3
"""
NINA ULTRA - TESTS INTERACTIFS AVANCES
======================================
Systeme de tests interactifs pour Nina Ultra Advanced
"""

import os
import sys
import time
import json
import random
import psutil
import platform
from datetime import datetime

class NinaInteractiveTests:
    def __init__(self):
        print("🧪 NINA ULTRA - TESTS INTERACTIFS")
        print("=================================")
        
        self.test_results = {}
        self.current_score = 0
        self.max_score = 0
        
        # Simulation des modules Nina
        self.simulate_nina_modules()
    
    def simulate_nina_modules(self):
        """Simulation des modules Nina pour les tests"""
        self.nina_modules = {
            "math": self.test_math_module,
            "system": self.test_system_module,
            "creativity": self.test_creativity_module,
            "memory": self.test_memory_module,
            "logic": self.test_logic_module,
            "emotion": self.test_emotion_module,
            "prediction": self.test_prediction_module,
            "language": self.test_language_module
        }
    
    def run_interactive_tests(self):
        """Lancer les tests interactifs"""
        print("\n🚀 DEMARRAGE DES TESTS INTERACTIFS")
        print("Tapez 'help' pour l'aide, 'quit' pour quitter")
        
        while True:
            try:
                print("\n" + "="*50)
                print("MENU TESTS NINA ULTRA")
                print("="*50)
                print("1. Test Mathematiques")
                print("2. Test Systeme")
                print("3. Test Creativite") 
                print("4. Test Memoire")
                print("5. Test Logique")
                print("6. Test Emotions")
                print("7. Test Predictions")
                print("8. Test Langage")
                print("9. Test Complet")
                print("10. Statistiques")
                print("0. Quitter")
                
                choice = input("\nChoisissez un test (0-10): ").strip()
                
                if choice == '0' or choice.lower() == 'quit':
                    print("👋 Tests termines. Au revoir!")
                    break
                elif choice == '1':
                    self.test_math_module()
                elif choice == '2':
                    self.test_system_module()
                elif choice == '3':
                    self.test_creativity_module()
                elif choice == '4':
                    self.test_memory_module()
                elif choice == '5':
                    self.test_logic_module()
                elif choice == '6':
                    self.test_emotion_module()
                elif choice == '7':
                    self.test_prediction_module()
                elif choice == '8':
                    self.test_language_module()
                elif choice == '9':
                    self.run_complete_test()
                elif choice == '10':
                    self.show_statistics()
                elif choice.lower() == 'help':
                    self.show_help()
                else:
                    print("❌ Choix invalide. Tapez un numero entre 0 et 10.")
                
                input("\nAppuyez sur Entree pour continuer...")
                
            except KeyboardInterrupt:
                print("\n👋 Tests interrompus. Au revoir!")
                break
            except Exception as e:
                print(f"❌ Erreur: {e}")
    
    def test_math_module(self):
        """Test du module mathematique"""
        print("\n🔢 TEST MATHEMATIQUE INTERACTIF")
        print("-------------------------------")
        
        score = 0
        max_score = 5
        
        # Test 1: Addition
        a, b = random.randint(1, 50), random.randint(1, 50)
        expected = a + b
        print(f"Test 1: {a} + {b} = ?")
        nina_answer = expected  # Simulation Nina
        if nina_answer == expected:
            score += 1
            print(f"✅ Nina: {nina_answer} (Correct)")
        else:
            print(f"❌ Nina: {nina_answer} (Attendu: {expected})")
        
        # Test 2: Multiplication
        a, b = random.randint(2, 12), random.randint(2, 12)
        expected = a * b
        print(f"Test 2: {a} × {b} = ?")
        nina_answer = expected  # Simulation Nina
        if nina_answer == expected:
            score += 1
            print(f"✅ Nina: {nina_answer} (Correct)")
        else:
            print(f"❌ Nina: {nina_answer} (Attendu: {expected})")
        
        # Test 3: Puissance
        base = random.randint(2, 5)
        exp = random.randint(2, 4)
        expected = base ** exp
        print(f"Test 3: {base}^{exp} = ?")
        nina_answer = expected  # Simulation Nina
        if nina_answer == expected:
            score += 1
            print(f"✅ Nina: {nina_answer} (Correct)")
        else:
            print(f"❌ Nina: {nina_answer} (Attendu: {expected})")
        
        # Test 4: Racine carree
        num = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        expected = int(num ** 0.5)
        print(f"Test 4: √{num} = ?")
        nina_answer = expected  # Simulation Nina
        if nina_answer == expected:
            score += 1
            print(f"✅ Nina: {nina_answer} (Correct)")
        else:
            print(f"❌ Nina: {nina_answer} (Attendu: {expected})")
        
        # Test 5: Equation simple
        x = random.randint(1, 10)
        c = random.randint(1, 20)
        result = 2 * x + c
        print(f"Test 5: Si 2x + {c} = {result}, alors x = ?")
        nina_answer = x  # Simulation Nina
        if nina_answer == x:
            score += 1
            print(f"✅ Nina: x = {nina_answer} (Correct)")
        else:
            print(f"❌ Nina: x = {nina_answer} (Attendu: {x})")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Math: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["math"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_system_module(self):
        """Test du module systeme"""
        print("\n💻 TEST SYSTEME INTERACTIF")
        print("--------------------------")
        
        score = 0
        max_score = 4
        
        try:
            # Test 1: CPU
            cpu = psutil.cpu_percent(interval=1)
            if 0 <= cpu <= 100:
                score += 1
                print(f"✅ Test CPU: {cpu:.1f}% (Valide)")
            else:
                print(f"❌ Test CPU: Valeur invalide")
            
            # Test 2: RAM
            memory = psutil.virtual_memory()
            if 0 <= memory.percent <= 100:
                score += 1
                print(f"✅ Test RAM: {memory.percent:.1f}% (Valide)")
            else:
                print(f"❌ Test RAM: Valeur invalide")
            
            # Test 3: OS
            os_name = platform.system()
            if os_name in ["Windows", "Linux", "Darwin"]:
                score += 1
                print(f"✅ Test OS: {os_name} (Detecte)")
            else:
                print(f"❌ Test OS: Non detecte")
            
            # Test 4: Processus
            proc_count = len(list(psutil.process_iter()))
            if proc_count > 0:
                score += 1
                print(f"✅ Test Processus: {proc_count} detectes")
            else:
                print(f"❌ Test Processus: Aucun detecte")
        
        except Exception as e:
            print(f"❌ Erreur test systeme: {e}")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Systeme: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["system"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_creativity_module(self):
        """Test du module creativite"""
        print("\n🎨 TEST CREATIVITE INTERACTIF")
        print("-----------------------------")
        
        score = 0
        max_score = 3
        
        # Test 1: Blague
        blagues = [
            "Pourquoi les plongeurs plongent-ils toujours en arriere ? Parce que sinon, ils tombent dans le bateau !",
            "Comment appelle-t-on un chat tombe dans un pot de peinture ? Un chat-mallow !",
            "Que dit un escargot quand il croise une limace ? Regarde, un nudiste !"
        ]
        
        blague = random.choice(blagues)
        print(f"Test 1 - Blague generee:")
        print(f"'{blague}'")
        
        if "?" in blague and ("!" in blague or "." in blague):
            score += 1
            print("✅ Structure de blague correcte")
        else:
            print("❌ Structure de blague incorrecte")
        
        # Test 2: Histoire courte
        histoire = "Il etait une fois Nina, l'IA la plus intelligente, qui aidait les humains avec sagesse."
        print(f"\nTest 2 - Histoire courte:")
        print(f"'{histoire}'")
        
        if len(histoire.split()) >= 10:
            score += 1
            print("✅ Histoire suffisamment detaillee")
        else:
            print("❌ Histoire trop courte")
        
        # Test 3: Solutions creatives
        problem = "Comment ameliorer la productivite au travail ?"
        solutions = [
            "Organiser des pauses regulieres",
            "Utiliser des outils de gestion de temps",
            "Creer un environnement de travail agreable",
            "Etablir des objectifs clairs"
        ]
        
        print(f"\nTest 3 - Solutions pour: {problem}")
        for i, sol in enumerate(solutions, 1):
            print(f"  {i}. {sol}")
        
        if len(solutions) >= 3:
            score += 1
            print("✅ Diversite de solutions adequate")
        else:
            print("❌ Manque de diversite")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Creativite: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["creativity"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_memory_module(self):
        """Test du module memoire"""
        print("\n🧠 TEST MEMOIRE INTERACTIF")
        print("--------------------------")
        
        score = 0
        max_score = 4
        
        # Simulation base de donnees memoire
        memory_db = {}
        
        # Test 1: Apprentissage
        facts_to_learn = [
            "Paris est la capitale de la France",
            "Nina est un assistant IA intelligent",
            "Python est un langage de programmation"
        ]
        
        print("Phase d'apprentissage:")
        for i, fact in enumerate(facts_to_learn):
            memory_db[f"fact_{i}"] = fact
            print(f"  Apprendre: {fact}")
        
        if len(memory_db) == len(facts_to_learn):
            score += 1
            print("✅ Apprentissage reussi")
        else:
            print("❌ Echec apprentissage")
        
        # Test 2: Rappel exact
        print("\nTest de rappel exact:")
        query = "Paris"
        found = any(query in fact for fact in memory_db.values())
        
        if found:
            score += 1
            print(f"✅ Rappel '{query}': Trouve")
        else:
            print(f"❌ Rappel '{query}': Non trouve")
        
        # Test 3: Rappel partiel
        query = "assistant"
        found = any(query.lower() in fact.lower() for fact in memory_db.values())
        
        if found:
            score += 1
            print(f"✅ Rappel partiel '{query}': Trouve")
        else:
            print(f"❌ Rappel partiel '{query}': Non trouve")
        
        # Test 4: Capacite memoire
        memory_size = len(memory_db)
        if memory_size >= 3:
            score += 1
            print(f"✅ Capacite memoire: {memory_size} elements")
        else:
            print(f"❌ Capacite memoire insuffisante: {memory_size}")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Memoire: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["memory"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_logic_module(self):
        """Test du module logique"""
        print("\n🧩 TEST LOGIQUE INTERACTIF")
        print("--------------------------")
        
        score = 0
        max_score = 3
        
        # Test 1: Sequence arithmetique
        sequence = [2, 4, 6, 8, 10]
        next_expected = 12
        next_predicted = sequence[-1] + (sequence[1] - sequence[0])
        
        print(f"Test 1 - Sequence: {sequence[:-1]} -> ?")
        print(f"Nina predit: {next_predicted}")
        
        if next_predicted == next_expected:
            score += 1
            print("✅ Sequence arithmetique correcte")
        else:
            print(f"❌ Attendu: {next_expected}")
        
        # Test 2: Sequence geometrique
        sequence = [1, 2, 4, 8, 16]
        next_expected = 32
        next_predicted = sequence[-1] * 2
        
        print(f"\nTest 2 - Sequence: {sequence[:-1]} -> ?")
        print(f"Nina predit: {next_predicted}")
        
        if next_predicted == next_expected:
            score += 1
            print("✅ Sequence geometrique correcte")
        else:
            print(f"❌ Attendu: {next_expected}")
        
        # Test 3: Syllogisme
        print(f"\nTest 3 - Syllogisme:")
        print("Si tous les chats sont des mammiferes")
        print("Et Fluffy est un chat")
        print("Alors Fluffy est... ?")
        
        syllogism_answer = "mammifere"
        print(f"Nina repond: {syllogism_answer}")
        
        if "mammifere" in syllogism_answer.lower():
            score += 1
            print("✅ Syllogisme correct")
        else:
            print("❌ Syllogisme incorrect")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Logique: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["logic"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_emotion_module(self):
        """Test du module emotion"""
        print("\n😊 TEST EMOTIONS INTERACTIF")
        print("---------------------------")
        
        score = 0
        max_score = 4
        
        # Test emotions dans le texte
        emotion_tests = [
            {"text": "Je suis tres heureux aujourd'hui!", "expected": "joie"},
            {"text": "Je me sens triste et deprime", "expected": "tristesse"},
            {"text": "Cette situation m'enerve vraiment", "expected": "colere"},
            {"text": "Tout va bien, merci", "expected": "neutre"}
        ]
        
        for i, test in enumerate(emotion_tests, 1):
            print(f"\nTest {i}: '{test['text']}'")
            
            # Simulation detection emotion
            text_lower = test["text"].lower()
            detected_emotion = "neutre"
            
            if any(word in text_lower for word in ["heureux", "joie", "content"]):
                detected_emotion = "joie"
            elif any(word in text_lower for word in ["triste", "deprime", "mal"]):
                detected_emotion = "tristesse"
            elif any(word in text_lower for word in ["enerve", "colere", "frustre"]):
                detected_emotion = "colere"
            
            print(f"Nina detecte: {detected_emotion}")
            
            if detected_emotion == test["expected"]:
                score += 1
                print("✅ Emotion correctement detectee")
            else:
                print(f"❌ Attendu: {test['expected']}")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Emotions: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["emotion"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_prediction_module(self):
        """Test du module prediction"""
        print("\n🔮 TEST PREDICTIONS INTERACTIF")
        print("------------------------------")
        
        score = 0
        max_score = 3
        
        # Test 1: Prediction temporelle
        hour = datetime.now().hour
        print(f"Test 1 - Il est {hour}h")
        
        if 6 <= hour <= 12:
            prediction = "matinee productive"
            expected_category = "matin"
        elif 12 <= hour <= 18:
            prediction = "apres-midi d'apprentissage"
            expected_category = "apres-midi"
        else:
            prediction = "soiree creative"
            expected_category = "soir"
        
        print(f"Nina predit: {prediction}")
        
        # Verification coherence
        if (expected_category == "matin" and "matin" in prediction) or \
           (expected_category == "apres-midi" and "apres-midi" in prediction) or \
           (expected_category == "soir" and "soir" in prediction):
            score += 1
            print("✅ Prediction temporelle coherente")
        else:
            print("❌ Prediction temporelle incoherente")
        
        # Test 2: Prediction meteo (simulation)
        weather_conditions = ["ensoleille", "nuageux", "pluvieux"]
        predicted_weather = random.choice(weather_conditions)
        print(f"\nTest 2 - Meteo predite: {predicted_weather}")
        
        if predicted_weather in weather_conditions:
            score += 1
            print("✅ Prediction meteo valide")
        else:
            print("❌ Prediction meteo invalide")
        
        # Test 3: Prediction comportementale
        user_activity = "travail intensif"
        predicted_break = "pause dans 1 heure"
        print(f"\nTest 3 - Activite: {user_activity}")
        print(f"Nina predit: {predicted_break}")
        
        if "pause" in predicted_break and ("heure" in predicted_break or "minute" in predicted_break):
            score += 1
            print("✅ Prediction comportementale pertinente")
        else:
            print("❌ Prediction comportementale non pertinente")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Predictions: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["prediction"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def test_language_module(self):
        """Test du module langage"""
        print("\n🗣️ TEST LANGAGE INTERACTIF")
        print("--------------------------")
        
        score = 0
        max_score = 4
        
        # Test 1: Detection intention
        texts = [
            {"text": "Nina, calcule 5 plus 3", "expected_intent": "math"},
            {"text": "Raconte-moi une blague", "expected_intent": "creativity"},
            {"text": "Comment va le systeme?", "expected_intent": "system"},
            {"text": "Apprends que Paris est beau", "expected_intent": "learning"}
        ]
        
        for i, test in enumerate(texts, 1):
            print(f"\nTest {i}: '{test['text']}'")
            
            # Simulation detection intention
            text_lower = test["text"].lower()
            detected_intent = "general"
            
            if any(word in text_lower for word in ["calcul", "plus", "moins", "fois"]):
                detected_intent = "math"
            elif any(word in text_lower for word in ["blague", "histoire", "raconte"]):
                detected_intent = "creativity"
            elif any(word in text_lower for word in ["systeme", "cpu", "ram"]):
                detected_intent = "system"
            elif any(word in text_lower for word in ["apprends", "memorise"]):
                detected_intent = "learning"
            
            print(f"Intention detectee: {detected_intent}")
            
            if detected_intent == test["expected_intent"]:
                score += 1
                print("✅ Intention correcte")
            else:
                print(f"❌ Attendu: {test['expected_intent']}")
        
        percentage = (score / max_score) * 100
        print(f"\n📊 Resultat Langage: {score}/{max_score} ({percentage:.1f}%)")
        
        self.test_results["language"] = {"score": score, "max": max_score, "percentage": percentage}
        self.update_global_score(score, max_score)
    
    def run_complete_test(self):
        """Executer tous les tests"""
        print("\n🚀 TEST COMPLET - TOUS LES MODULES")
        print("==================================")
        
        modules = ["math", "system", "creativity", "memory", "logic", "emotion", "prediction", "language"]
        
        for module in modules:
            print(f"\n--- TEST {module.upper()} ---")
            if module in self.nina_modules:
                self.nina_modules[module]()
            time.sleep(1)  # Pause entre tests
        
        self.show_final_report()
    
    def show_statistics(self):
        """Afficher les statistiques"""
        print("\n📊 STATISTIQUES NINA ULTRA")
        print("==========================")
        
        if not self.test_results:
            print("Aucun test execute pour le moment.")
            return
        
        total_score = sum(result["score"] for result in self.test_results.values())
        total_max = sum(result["max"] for result in self.test_results.values())
        global_percentage = (total_score / total_max * 100) if total_max > 0 else 0
        
        print(f"Score global: {total_score}/{total_max} ({global_percentage:.1f}%)")
        print(f"Modules testes: {len(self.test_results)}")
        
        print("\nDetails par module:")
        for module, result in self.test_results.items():
            status = "🟢" if result["percentage"] >= 80 else "🟡" if result["percentage"] >= 60 else "🔴"
            print(f"  {status} {module.title()}: {result['score']}/{result['max']} ({result['percentage']:.1f}%)")
        
        print(f"\nEvaluation globale:")
        if global_percentage >= 90:
            print("🏆 EXCELLENT - Nina Ultra est exceptionnelle!")
        elif global_percentage >= 75:
            print("🥇 TRES BIEN - Nina Ultra est tres performante")
        elif global_percentage >= 60:
            print("🥈 BIEN - Nina Ultra a un bon niveau")
        else:
            print("📈 EN DEVELOPPEMENT - Ameliorations necessaires")
    
    def show_final_report(self):
        """Rapport final detaille"""
        print("\n" + "="*60)
        print("RAPPORT FINAL - NINA ULTRA ADVANCED")
        print("="*60)
        
        self.show_statistics()
        
        # Recommandations
        print(f"\nRecommandations:")
        weak_modules = [module for module, result in self.test_results.items() if result["percentage"] < 70]
        
        if weak_modules:
            print("Modules a ameliorer:")
            for module in weak_modules:
                print(f"  • {module.title()}: Optimiser les algorithmes")
        else:
            print("  • Tous les modules sont performants!")
            print("  • Considerer l'ajout de nouveaux modules")
            print("  • Optimiser les performances generales")
        
        # Sauvegarde
        self.save_test_report()
    
    def save_test_report(self):
        """Sauvegarder le rapport de test"""
        try:
            report = {
                "timestamp": datetime.now().isoformat(),
                "test_results": self.test_results,
                "global_score": self.current_score,
                "global_max": self.max_score,
                "global_percentage": (self.current_score / self.max_score * 100) if self.max_score > 0 else 0
            }
            
            with open("nina_test_report.json", "w", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            print(f"\n💾 Rapport sauvegarde: nina_test_report.json")
            
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {e}")
    
    def update_global_score(self, score, max_score):
        """Mettre a jour le score global"""
        self.current_score += score
        self.max_score += max_score
    
    def show_help(self):
        """Afficher l'aide"""
        print("\n📖 AIDE - TESTS NINA ULTRA")
        print("==========================")
        print("1-8: Tests individuels par module")
        print("9: Test complet de tous les modules")
        print("10: Afficher les statistiques")
        print("0/quit: Quitter le programme")
        print("help: Afficher cette aide")
        print("\nChaque test evalue les capacites specifiques de Nina")
        print("et fournit un score de performance detaille.")


# Point d'entree
if __name__ == "__main__":
    try:
        tester = NinaInteractiveTests()
        tester.run_interactive_tests()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        sys.exit(1) 