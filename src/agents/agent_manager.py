#!/usr/bin/env python3
"""
🎯 Agent Manager - Gestionnaire intelligent des agents IA spécialisés
"""

import time
from typing import List, Dict, Optional
from .math_agent import MathAgent
from .knowledge_agent import KnowledgeAgent
from .system_agent import SystemAgent

class AgentManager:
    """Gestionnaire intelligent des agents IA spécialisés"""
    
    def __init__(self):
        self.agents = []
        self.performance_stats = {
            "total_requests": 0,
            "agent_usage": {},
            "avg_response_time": 0.0,
            "cache_hit_rate": 0.0
        }
        
        # Initialiser les agents
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialise tous les agents spécialisés"""
        try:
            # Agent mathématiques
            self.agents.append(MathAgent())
            
            # Agent connaissances générales
            self.agents.append(KnowledgeAgent())
            
            # Agent système
            self.agents.append(SystemAgent())
            
            print(f"✅ {len(self.agents)} agents initialisés avec succès")
            
        except Exception as e:
            print(f"❌ Erreur initialisation agents : {e}")
    
    def find_best_agent(self, query: str) -> Optional[object]:
        """Trouve le meilleur agent pour traiter la requête"""
        
        # Tester chaque agent
        candidates = []
        for agent in self.agents:
            try:
                if agent.can_handle(query):
                    # Score basé sur la spécialisation et performance
                    score = self._calculate_agent_score(agent, query)
                    candidates.append((agent, score))
            except Exception as e:
                print(f"⚠️ Erreur évaluation agent {agent.name}: {e}")
                continue
        
        if not candidates:
            return None
        
        # Retourner l'agent avec le meilleur score
        best_agent = max(candidates, key=lambda x: x[1])[0]
        return best_agent
    
    def _calculate_agent_score(self, agent, query: str) -> float:
        """Calcule un score pour un agent selon la requête"""
        score = 1.0  # Score de base
        
        # Bonus pour les performances passées
        if agent.performance_stats["requests"] > 0:
            # Bonus pour temps de réponse rapide
            if agent.performance_stats["avg_response_time"] < 100:  # < 100ms
                score += 0.5
            
            # Bonus pour taux de cache élevé
            cache_rate = agent.performance_stats["cache_hits"] / agent.performance_stats["requests"]
            score += cache_rate * 0.3
        
        # Bonus spécifique par type d'agent
        query_lower = query.lower()
        
        if isinstance(agent, MathAgent):
            # Bonus pour requêtes mathématiques évidentes
            if any(op in query_lower for op in ['+', '-', '*', '/', '=', 'calcul']):
                score += 1.0
        
        elif isinstance(agent, SystemAgent):
            # Bonus pour requêtes système évidentes
            if any(word in query_lower for word in ['cpu', 'ram', 'disk', 'système', 'info']):
                score += 1.0
        
        elif isinstance(agent, KnowledgeAgent):
            # Bonus pour questions complexes
            if any(word in query_lower for word in ['pourquoi', 'comment', 'qu\'est-ce']):
                score += 0.8
        
        return score
    
    def process_query(self, query: str) -> Dict:
        """Traite une requête via le meilleur agent"""
        start_time = time.time()
        
        # Statistiques
        self.performance_stats["total_requests"] += 1
        
        # Trouver le meilleur agent
        best_agent = self.find_best_agent(query)
        
        if not best_agent:
            return {
                "response": "🤔 Aucun agent spécialisé trouvé pour cette requête. Essayez une question plus spécifique !",
                "agent": "AgentManager",
                "cached": False,
                "response_time": (time.time() - start_time) * 1000,
                "confidence": 0.0
            }
        
        # Exécuter l'agent
        try:
            result = best_agent.execute(query)
            
            # Mettre à jour les statistiques
            agent_name = best_agent.name
            if agent_name not in self.performance_stats["agent_usage"]:
                self.performance_stats["agent_usage"][agent_name] = 0
            self.performance_stats["agent_usage"][agent_name] += 1
            
            # Calculer la confiance
            confidence = self._calculate_confidence(best_agent, query, result)
            result["confidence"] = confidence
            
            return result
            
        except Exception as e:
            return {
                "response": f"❌ Erreur lors du traitement par {best_agent.name}: {str(e)}",
                "agent": best_agent.name,
                "cached": False,
                "response_time": (time.time() - start_time) * 1000,
                "confidence": 0.0
            }
    
    def _calculate_confidence(self, agent, query: str, result: Dict) -> float:
        """Calcule le niveau de confiance de la réponse"""
        confidence = 0.5  # Confiance de base
        
        # Bonus si réponse du cache (déjà validée)
        if result.get("cached", False):
            confidence += 0.3
        
        # Bonus si temps de réponse rapide
        if result.get("response_time", 1000) < 50:  # < 50ms
            confidence += 0.2
        
        # Bonus spécifique par type d'agent
        if isinstance(agent, MathAgent):
            # Math a une confiance élevée pour les calculs simples
            if any(op in query.lower() for op in ['+', '-', '*', '/']):
                confidence += 0.3
        
        elif isinstance(agent, SystemAgent):
            # System a une confiance élevée pour les infos système
            confidence += 0.3
        
        # Limiter entre 0 et 1
        return min(1.0, max(0.0, confidence))
    
    def get_agent_status(self) -> Dict:
        """Retourne le statut de tous les agents"""
        status = {
            "manager_stats": self.performance_stats,
            "agents": []
        }
        
        for agent in self.agents:
            try:
                agent_status = agent.get_status()
                status["agents"].append(agent_status)
            except Exception as e:
                status["agents"].append({
                    "name": getattr(agent, 'name', 'Unknown'),
                    "error": str(e)
                })
        
        return status
    
    def get_agent_list(self) -> List[str]:
        """Retourne la liste des agents disponibles"""
        return [f"{agent.name} ({agent.speciality})" for agent in self.agents]
    
    def clear_all_caches(self):
        """Vide le cache de tous les agents"""
        cleared = 0
        for agent in self.agents:
            try:
                cache_size = len(agent.cache)
                agent.cache.clear()
                cleared += cache_size
            except:
                pass
        
        return f"🧹 {cleared} entrées de cache supprimées"
    
    def get_performance_summary(self) -> str:
        """Retourne un résumé des performances"""
        stats = self.performance_stats
        
        summary = f"""📊 **PERFORMANCES AGENT MANAGER**
🎯 Requêtes totales : {stats['total_requests']}
⚡ Temps moyen : {stats.get('avg_response_time', 0):.1f}ms

🤖 **UTILISATION AGENTS**"""
        
        for agent_name, count in stats["agent_usage"].items():
            percentage = (count / stats["total_requests"] * 100) if stats["total_requests"] > 0 else 0
            summary += f"\n• {agent_name}: {count} ({percentage:.1f}%)"
        
        return summary 