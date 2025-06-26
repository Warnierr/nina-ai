#!/usr/bin/env python3
"""
🤖 Base Agent - Classe de base pour tous les agents IA de Nina
"""

import json
import time
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from rich.console import Console

console = Console()

class BaseAgent(ABC):
    """Classe de base pour tous les agents IA de Nina"""
    
    def __init__(self, name: str, speciality: str):
        self.name = name
        self.speciality = speciality
        self.created_at = datetime.now()
        self.cache = {}
        self.performance_stats = {
            "requests": 0,
            "cache_hits": 0,
            "avg_response_time": 0.0
        }
    
    @abstractmethod
    def can_handle(self, query: str) -> bool:
        """Détermine si cet agent peut traiter la requête"""
        pass
    
    @abstractmethod
    def process(self, query: str) -> str:
        """Traite la requête et retourne une réponse"""
        pass
    
    def get_cache_key(self, query: str) -> str:
        """Génère une clé de cache pour la requête"""
        return hashlib.md5(f"{self.name}:{query.lower()}".encode()).hexdigest()
    
    def get_cached_response(self, query: str) -> str:
        """Récupère une réponse du cache si disponible"""
        cache_key = self.get_cache_key(query)
        if cache_key in self.cache:
            self.performance_stats["cache_hits"] += 1
            return self.cache[cache_key]
        return None
    
    def cache_response(self, query: str, response: str):
        """Met en cache une réponse"""
        cache_key = self.get_cache_key(query)
        self.cache[cache_key] = response
    
    def execute(self, query: str) -> dict:
        """Exécute l'agent avec mesure de performance"""
        start_time = time.time()
        
        # Vérifier le cache d'abord
        cached = self.get_cached_response(query)
        if cached:
            return {
                "response": cached,
                "agent": self.name,
                "cached": True,
                "response_time": 0.0
            }
        
        # Traiter la requête
        response = self.process(query)
        
        # Mesurer le temps
        response_time = (time.time() - start_time) * 1000  # en ms
        
        # Mettre à jour les stats
        self.performance_stats["requests"] += 1
        self.performance_stats["avg_response_time"] = (
            (self.performance_stats["avg_response_time"] * (self.performance_stats["requests"] - 1) + response_time) /
            self.performance_stats["requests"]
        )
        
        # Mettre en cache
        self.cache_response(query, response)
        
        return {
            "response": response,
            "agent": self.name,
            "cached": False,
            "response_time": response_time
        }
    
    def get_status(self) -> dict:
        """Retourne le statut de l'agent"""
        return {
            "name": self.name,
            "speciality": self.speciality,
            "uptime": str(datetime.now() - self.created_at),
            "performance": self.performance_stats,
            "cache_size": len(self.cache)
        } 