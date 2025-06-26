#!/usr/bin/env python3
"""
🧠 Knowledge Agent - Agent spécialisé en connaissances générales
"""

import requests
import json
from .base_agent import BaseAgent

class KnowledgeAgent(BaseAgent):
    """Agent spécialisé en connaissances générales et questions complexes"""
    
    def __init__(self):
        super().__init__("KnowledgeAgent", "Connaissances générales")
        
        # Base de connaissances rapides
        self.knowledge_base = {
            "pourquoi le ciel est bleu": "Le ciel est bleu à cause de la diffusion de Rayleigh. Les molécules d'air diffusent plus la lumière bleue que les autres couleurs.",
            "qu'est-ce que l'ia": "L'Intelligence Artificielle (IA) est une technologie qui permet aux machines de simuler l'intelligence humaine.",
            "comment fonctionne internet": "Internet fonctionne grâce à un réseau mondial d'ordinateurs connectés qui échangent des données via des protocoles comme TCP/IP.",
            "qu'est-ce que python": "Python est un langage de programmation interprété, orienté objet, avec une syntaxe claire et lisible.",
            "qu'est-ce que linux": "Linux est un système d'exploitation open-source basé sur Unix, très utilisé pour les serveurs et le développement.",
            "comment marche un ordinateur": "Un ordinateur traite l'information via le CPU, stocke les données en mémoire (RAM/disque), et utilise des périphériques pour l'entrée/sortie.",
        }
        
        # Catégories de questions
        self.categories = {
            "science": ["pourquoi", "comment", "qu'est-ce que", "expliquer"],
            "technologie": ["ordinateur", "internet", "logiciel", "programmation", "ia", "intelligence artificielle"],
            "général": ["qui", "quoi", "où", "quand", "combien"]
        }
    
    def can_handle(self, query: str) -> bool:
        """Détermine si cette requête nécessite des connaissances générales"""
        query_clean = query.lower().strip()
        
        # Vérifier la base de connaissances
        if query_clean in self.knowledge_base:
            return True
        
        # Vérifier les mots-clés de questions
        question_words = ["pourquoi", "comment", "qu'est-ce", "expliquer", "définir", "qui est", "que signifie"]
        if any(word in query_clean for word in question_words):
            return True
        
        # Vérifier les domaines de connaissance
        for category, keywords in self.categories.items():
            if any(keyword in query_clean for keyword in keywords):
                return True
        
        return False
    
    def process(self, query: str) -> str:
        """Traite les requêtes de connaissances"""
        query_clean = query.lower().strip()
        
        # Réponses rapides de la base de connaissances
        if query_clean in self.knowledge_base:
            return f"📚 {self.knowledge_base[query_clean]}"
        
        # Analyse du type de question
        if "pourquoi" in query_clean:
            return self._handle_why_question(query)
        elif "comment" in query_clean:
            return self._handle_how_question(query)
        elif "qu'est-ce" in query_clean or "définir" in query_clean:
            return self._handle_definition_question(query)
        elif any(tech in query_clean for tech in self.categories["technologie"]):
            return self._handle_tech_question(query)
        else:
            return self._provide_general_guidance(query)
    
    def _handle_why_question(self, query: str) -> str:
        """Gère les questions 'pourquoi'"""
        responses = [
            f"🤔 Excellente question ! '{query}' touche à des concepts complexes.",
            "💡 Pour une réponse complète, je recommande de consulter des sources spécialisées.",
            "🔍 Cette question mérite une recherche approfondie pour une réponse précise."
        ]
        
        # Réponses spécifiques selon le sujet
        if "ciel" in query.lower():
            return "🌌 Le ciel est bleu à cause de la diffusion de Rayleigh : les molécules d'air diffusent plus la lumière bleue."
        elif "ordinateur" in query.lower():
            return "💻 Les ordinateurs fonctionnent grâce aux circuits électroniques qui traitent l'information en binaire (0 et 1)."
        
        return responses[0]
    
    def _handle_how_question(self, query: str) -> str:
        """Gère les questions 'comment'"""
        if "marche" in query.lower() or "fonctionne" in query.lower():
            if "ordinateur" in query.lower():
                return "💻 Un ordinateur fonctionne via : CPU (calculs), RAM (mémoire), stockage (disque), et périphériques (entrée/sortie)."
            elif "internet" in query.lower():
                return "🌐 Internet fonctionne via un réseau mondial utilisant TCP/IP pour échanger des données entre serveurs."
        
        return f"🛠️ Pour comprendre '{query}', il faut analyser les étapes et mécanismes impliqués."
    
    def _handle_definition_question(self, query: str) -> str:
        """Gère les questions de définition"""
        if "ia" in query.lower() or "intelligence artificielle" in query.lower():
            return "🤖 L'IA est une technologie permettant aux machines de simuler l'intelligence humaine (apprentissage, raisonnement, perception)."
        elif "python" in query.lower():
            return "🐍 Python est un langage de programmation interprété, orienté objet, réputé pour sa syntaxe claire et sa polyvalence."
        elif "linux" in query.lower():
            return "🐧 Linux est un système d'exploitation open-source basé sur Unix, très utilisé pour les serveurs et le développement."
        
        return f"📖 '{query}' nécessite une définition précise que je peux rechercher pour vous."
    
    def _handle_tech_question(self, query: str) -> str:
        """Gère les questions technologiques"""
        return "💻 Question technologique détectée ! Je peux expliquer les concepts de base en informatique, programmation et IA."
    
    def _provide_general_guidance(self, query: str) -> str:
        """Fournit des conseils généraux"""
        return f"🎯 Question intéressante : '{query}'. Je peux vous aider avec des connaissances générales, sciences, et technologie !"
    
    def search_external_knowledge(self, query: str) -> str:
        """Recherche des connaissances externes (pour future intégration API)"""
        # Placeholder pour intégration future avec APIs de recherche
        return f"🔍 Recherche externe pour : {query} (à implémenter avec APIs)" 