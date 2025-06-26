#!/usr/bin/env python3
"""
🧠 Nina Advanced AI - Version avec Agents IA Spécialisés
Système multi-agents intelligent avec spécialisations
"""

import json
import time
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Import des agents (avec gestion d'erreurs)
try:
    from agents.agent_manager import AgentManager
    AGENTS_AVAILABLE = True
except ImportError:
    AGENTS_AVAILABLE = False
    print("⚠️ Agents non disponibles, mode de base activé")

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
CACHE_DIR = PROJECT_ROOT / "cache"
CONFIG_DIR = PROJECT_ROOT / "config"
CACHE_FILE = CACHE_DIR / "nina_advanced_cache.json"

# Créer dossiers
CACHE_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)

console = Console()

class NinaAdvanced:
    """Nina Advanced - IA avec agents spécialisés"""
    
    def __init__(self):
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.cache = {}
        self.agent_manager = None
        
        # Réponses de base (fallback)
        self.basic_responses = {
            "bonjour": "Bonjour ! Je suis Nina Advanced avec agents IA spécialisés ! 🧠🤖",
            "salut": "Salut ! Mes agents IA sont prêts à vous aider !",
            "qui es-tu": "Je suis Nina Advanced, assistante IA avec système multi-agents spécialisés !",
            "aide": "Je dispose d'agents spécialisés : Math, Connaissances, Système. Posez votre question !",
            "agents": "Mes agents : 🔢 Math, 🧠 Connaissances, ⚙️ Système",
        }
        
        # Initialiser les agents
        self._initialize_agents()
        self._load_cache()
    
    def _initialize_agents(self):
        """Initialise le système d'agents"""
        if AGENTS_AVAILABLE:
            try:
                self.agent_manager = AgentManager()
                console.print("✅ [green]Système d'agents initialisé avec succès[/green]")
            except Exception as e:
                console.print(f"❌ [red]Erreur initialisation agents: {e}[/red]")
                self.agent_manager = None
        else:
            console.print("⚠️ [yellow]Mode de base sans agents spécialisés[/yellow]")
    
    def _load_cache(self):
        """Charge le cache depuis le fichier"""
        try:
            if CACHE_FILE.exists():
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
        except Exception as e:
            console.print(f"⚠️ [yellow]Erreur chargement cache: {e}[/yellow]")
            self.cache = {}
    
    def _save_cache(self):
        """Sauvegarde le cache"""
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            console.print(f"⚠️ [yellow]Erreur sauvegarde cache: {e}[/yellow]")
    
    def get_response(self, query: str) -> str:
        """Obtient une réponse intelligente"""
        start_time = time.time()
        
        # Vérifier le cache local d'abord
        cache_key = query.lower().strip()
        if cache_key in self.cache:
            response_time = (time.time() - start_time) * 1000
            return f"{self.cache[cache_key]} ⚡ (cache: {response_time:.1f}ms)"
        
        # Réponses de base rapides
        if cache_key in self.basic_responses:
            response = self.basic_responses[cache_key]
            response_time = (time.time() - start_time) * 1000
            return f"{response} ⚡ ({response_time:.1f}ms)"
        
        # Utiliser les agents si disponibles
        if self.agent_manager:
            try:
                result = self.agent_manager.process_query(query)
                
                # Ajouter les métriques
                confidence_emoji = "🎯" if result.get("confidence", 0) > 0.7 else "🤔"
                agent_name = result.get("agent", "Unknown")
                response_time = result.get("response_time", 0)
                cached_status = "📋" if result.get("cached", False) else "🔄"
                
                full_response = f"{result['response']}\n\n{confidence_emoji} Agent: {agent_name} | {cached_status} {response_time:.1f}ms"
                
                # Mettre en cache les bonnes réponses
                if result.get("confidence", 0) > 0.6:
                    self.cache[cache_key] = result['response']
                    self._save_cache()
                
                return full_response
                
            except Exception as e:
                return f"❌ Erreur agents: {str(e)}"
        
        # Fallback sans agents
        return f"🤔 Question intéressante ! (Mode de base - agents non disponibles)"
    
    def display_header(self):
        """Affiche l'en-tête Nina Advanced"""
        header_text = Text()
        header_text.append("🧠 NINA ADVANCED AI 🤖\n", style="bold magenta")
        header_text.append("Intelligence Multi-Agents Spécialisés\n", style="cyan")
        
        if self.agent_manager:
            agents = self.agent_manager.get_agent_list()
            header_text.append(f"Agents actifs: {len(agents)}\n", style="green")
            for agent in agents:
                header_text.append(f"• {agent}\n", style="dim")
        else:
            header_text.append("Mode de base (agents non disponibles)\n", style="yellow")
        
        panel = Panel(
            header_text,
            title="[bold blue]🚀 Nina Advanced[/bold blue]",
            border_style="magenta"
        )
        console.print(panel)
    
    def show_agents_status(self):
        """Affiche le statut des agents"""
        if not self.agent_manager:
            console.print("❌ [red]Aucun agent disponible[/red]")
            return
        
        try:
            status = self.agent_manager.get_agent_status()
            
            # Tableau des agents
            table = Table(title="🤖 Statut des Agents IA")
            table.add_column("Agent", style="cyan")
            table.add_column("Spécialité", style="magenta")
            table.add_column("Requêtes", style="green")
            table.add_column("Cache", style="yellow")
            table.add_column("Temps moy.", style="blue")
            
            for agent_info in status["agents"]:
                if "error" in agent_info:
                    table.add_row(
                        agent_info.get("name", "Unknown"),
                        "❌ Erreur",
                        "-", "-", "-"
                    )
                else:
                    perf = agent_info.get("performance", {})
                    table.add_row(
                        agent_info.get("name", "Unknown"),
                        agent_info.get("speciality", "Unknown"),
                        str(perf.get("requests", 0)),
                        str(agent_info.get("cache_size", 0)),
                        f"{perf.get('avg_response_time', 0):.1f}ms"
                    )
            
            console.print(table)
            
            # Résumé des performances
            console.print("\n" + self.agent_manager.get_performance_summary())
            
        except Exception as e:
            console.print(f"❌ [red]Erreur statut agents: {e}[/red]")
    
    def run(self):
        """Boucle principale Nina Advanced"""
        console.clear()
        self.display_header()
        
        console.print("\n[bold green]🚀 Nina Advanced prête ! Agents IA spécialisés activés[/bold green]")
        console.print("[dim]💡 Essayez: 2+3, pourquoi le ciel est bleu, cpu info, agents status[/dim]\n")
        
        while True:
            try:
                query = console.input("\n[bold cyan]🎤 Vous:[/bold cyan] ")
                
                if query.lower() in ['quit', 'exit', 'bye']:
                    console.print("\n[bold magenta]👋 À bientôt ! Nina Advanced s'arrête...[/bold magenta]")
                    break
                
                if query.lower() == 'agents':
                    self.show_agents_status()
                    continue
                
                if query.lower() == 'clear':
                    console.clear()
                    self.display_header()
                    continue
                
                if query.lower() == 'cache clear':
                    if self.agent_manager:
                        result = self.agent_manager.clear_all_caches()
                        console.print(f"✅ [green]{result}[/green]")
                    self.cache.clear()
                    self._save_cache()
                    console.print("✅ [green]Cache principal vidé[/green]")
                    continue
                
                # Traitement intelligent
                response = self.get_response(query)
                
                # Affichage avec style
                panel = Panel(
                    response,
                    title="[bold green]🧠 Nina Advanced[/bold green]",
                    border_style="green"
                )
                console.print(panel)
                
            except KeyboardInterrupt:
                console.print("\n[bold red]👋 Interruption détectée![/bold red]")
                break
            except Exception as e:
                console.print(f"\n[bold red]❌ Erreur: {e}[/bold red]")

def main():
    """Point d'entrée principal"""
    nina = NinaAdvanced()
    nina.run()

if __name__ == "__main__":
    main() 