#!/usr/bin/env python3
"""
🔢 Math Agent - Agent spécialisé en mathématiques et calculs
"""

import re
import math
from typing import Optional
from .base_agent import BaseAgent

class MathAgent(BaseAgent):
    """Agent spécialisé en mathématiques et calculs"""
    
    def __init__(self):
        super().__init__("MathAgent", "Mathématiques et calculs")
        self.math_patterns = [
            r'\d+\s*[\+\-\*\/]\s*\d+',  # Opérations simples
            r'sqrt\(\d+\)',             # Racine carrée
            r'pow\(\d+,\s*\d+\)',       # Puissance
            r'sin\(\d+\)',              # Sinus
            r'cos\(\d+\)',              # Cosinus
            r'tan\(\d+\)',              # Tangente
        ]
        
        # Réponses rapides pour calculs courants
        self.quick_math = {
            "2+2": "2 + 2 = 4",
            "2+3": "2 + 3 = 5",
            "3+3": "3 + 3 = 6",
            "5*3": "5 × 3 = 15",
            "10/2": "10 ÷ 2 = 5",
            "2*8": "2 × 8 = 16",
            "100-50": "100 - 50 = 50",
        }
    
    def can_handle(self, query: str) -> bool:
        """Détermine si cette requête est mathématique"""
        query_clean = query.lower().strip()
        
        # Vérifier les calculs rapides
        if query_clean in self.quick_math:
            return True
        
        # Vérifier les patterns mathématiques
        for pattern in self.math_patterns:
            if re.search(pattern, query_clean):
                return True
        
        # Mots-clés mathématiques
        math_keywords = [
            'calcul', 'calculer', 'combien', 'résultat', 'somme', 
            'produit', 'différence', 'quotient', 'racine', 'puissance',
            'sinus', 'cosinus', 'tangente', 'logarithme'
        ]
        
        return any(keyword in query_clean for keyword in math_keywords)
    
    def process(self, query: str) -> str:
        """Traite les requêtes mathématiques"""
        query_clean = query.lower().strip()
        
        # Réponses rapides
        if query_clean in self.quick_math:
            return f"⚡ {self.quick_math[query_clean]} (calcul instantané)"
        
        try:
            # Extraction et évaluation d'expressions simples
            result = self._evaluate_expression(query_clean)
            if result is not None:
                return f"🔢 Résultat : {result}"
            
            # Fonctions mathématiques avancées
            if 'sqrt' in query_clean:
                return self._handle_sqrt(query_clean)
            
            if any(func in query_clean for func in ['sin', 'cos', 'tan']):
                return self._handle_trigonometry(query_clean)
            
            return "🤔 Je peux calculer des expressions comme 2+3, sqrt(16), sin(30), etc."
            
        except Exception as e:
            return f"❌ Erreur de calcul : {str(e)}"
    
    def _evaluate_expression(self, expr: str) -> Optional[float]:
        """Évalue une expression mathématique simple"""
        # Nettoyer l'expression
        expr = re.sub(r'[^\d\+\-\*\/\.\(\)]', '', expr)
        
        if not expr:
            return None
        
        try:
            # Sécuriser l'évaluation
            allowed_chars = set('0123456789+-*/.() ')
            if all(c in allowed_chars for c in expr):
                result = eval(expr)
                return round(result, 6) if isinstance(result, float) else result
        except:
            pass
        
        return None
    
    def _handle_sqrt(self, query: str) -> str:
        """Gère les calculs de racine carrée"""
        match = re.search(r'sqrt\((\d+)\)', query)
        if match:
            number = int(match.group(1))
            result = math.sqrt(number)
            return f"√{number} = {result:.6f}"
        return "Format: sqrt(nombre)"
    
    def _handle_trigonometry(self, query: str) -> str:
        """Gère les fonctions trigonométriques"""
        for func in ['sin', 'cos', 'tan']:
            pattern = f'{func}\\((\\d+)\\)'
            match = re.search(pattern, query)
            if match:
                angle = int(match.group(1))
                radians = math.radians(angle)
                
                if func == 'sin':
                    result = math.sin(radians)
                elif func == 'cos':
                    result = math.cos(radians)
                else:  # tan
                    result = math.tan(radians)
                
                return f"{func}({angle}°) = {result:.6f}"
        
        return "Format: sin(angle), cos(angle), tan(angle)" 