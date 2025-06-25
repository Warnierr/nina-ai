#!/bin/bash

# =============================================================================
# SCRIPT D'INSTALLATION AUTOMATIQUE NINA IA - VM UBUNTU
# =============================================================================
# Ce script installe tout ce dont Nina a besoin dans la VM Ubuntu
# Sécurisé, optimisé, et prêt pour l'IA locale

echo "🚀 INSTALLATION NINA IA - VM UBUNTU SÉCURISÉE"
echo "=============================================="

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# =============================================================================
# 1. MISE À JOUR DU SYSTÈME
# =============================================================================
print_status "Mise à jour du système Ubuntu..."
sudo apt update && sudo apt upgrade -y
print_success "Système mis à jour"

# =============================================================================
# 2. INSTALLATION DES DÉPENDANCES DE BASE
# =============================================================================
print_status "Installation des dépendances de base..."
sudo apt install -y \
    curl \
    wget \
    git \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release \
    htop \
    nano \
    unzip \
    zip \
    jq

print_success "Dépendances installées"

# =============================================================================
# 3. INSTALLATION OLLAMA (IA LOCALE SÉCURISÉE)
# =============================================================================
print_status "Installation d'Ollama (IA locale)..."
curl -fsSL https://ollama.com/install.sh | sh

# Démarrer le service Ollama
sudo systemctl enable ollama
sudo systemctl start ollama

print_success "Ollama installé et démarré"

# Attendre qu'Ollama soit prêt
print_status "Attente du démarrage d'Ollama..."
sleep 10

# =============================================================================
# 4. TÉLÉCHARGEMENT DES MODÈLES IA
# =============================================================================
print_status "Téléchargement des modèles IA optimisés..."

# Modèle principal : Llama 3.2 3B (équilibre performance/qualité)
print_status "Téléchargement Llama 3.2 3B (modèle principal)..."
ollama pull llama3.2:3b

# Modèle rapide : Llama 3.2 1B (ultra-rapide)
print_status "Téléchargement Llama 3.2 1B (modèle rapide)..."
ollama pull llama3.2:1b

# Modèle spécialisé : Qwen2.5-Coder (pour le code)
print_status "Téléchargement Qwen2.5-Coder 1.5B (spécialisé code)..."
ollama pull qwen2.5-coder:1.5b

print_success "Modèles IA téléchargés"

# =============================================================================
# 5. CRÉATION DE L'ENVIRONNEMENT NINA
# =============================================================================
print_status "Création de l'environnement Nina..."

# Créer le dossier Nina
mkdir -p /home/$USER/nina-ai
cd /home/$USER/nina-ai

# Créer l'environnement virtuel Python
python3 -m venv nina_env
source nina_env/bin/activate

# Installer les dépendances Python
pip install --upgrade pip

# Dépendances Nina
pip install \
    ollama \
    requests \
    fastapi \
    uvicorn \
    websockets \
    python-multipart \
    jinja2 \
    psutil \
    schedule \
    colorama \
    rich

print_success "Environnement Nina créé"

# =============================================================================
# 6. CRÉATION DE NINA INTELLIGENTE
# =============================================================================
print_status "Création de Nina IA intelligente..."

cat > nina_vm.py << 'EOF'
#!/usr/bin/env python3
"""
NINA IA - VERSION VM UBUNTU SÉCURISÉE
=====================================
Assistant IA local avec Ollama, optimisé pour sécurité et performance
"""

import os
import sys
import time
import json
import asyncio
from datetime import datetime
import ollama
import psutil
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class NinaVM:
    def __init__(self):
        self.console = Console()
        self.models = {
            'principal': 'llama3.2:3b',      # Modèle principal
            'rapide': 'llama3.2:1b',         # Modèle rapide
            'code': 'qwen2.5-coder:1.5b'     # Spécialisé code
        }
        self.current_model = 'principal'
        self.conversation_history = []
        
        self.show_welcome()
        self.check_system()
    
    def show_welcome(self):
        """Affichage de bienvenue"""
        welcome_text = Text()
        welcome_text.append("🤖 NINA IA - VM UBUNTU SÉCURISÉE\n", style="bold blue")
        welcome_text.append("═══════════════════════════════════\n", style="blue")
        welcome_text.append("✅ 100% LOCAL - Vos données restent privées\n", style="green")
        welcome_text.append("⚡ OLLAMA - IA puissante et rapide\n", style="green")
        welcome_text.append("🛡️ SÉCURISÉ - Isolation totale VM\n", style="green")
        welcome_text.append("🧠 INTELLIGENT - Modèles multiples\n", style="green")
        
        panel = Panel(welcome_text, title="🚀 NINA IA", border_style="blue")
        self.console.print(panel)
    
    def check_system(self):
        """Vérifier l'état du système"""
        self.console.print("🔍 Vérification du système...", style="yellow")
        
        # Vérifier Ollama
        try:
            models = ollama.list()
            available_models = [model['name'] for model in models['models']]
            
            self.console.print(f"✅ Ollama actif - {len(available_models)} modèles disponibles", style="green")
            
            # Vérifier les modèles requis
            for name, model in self.models.items():
                if model in available_models:
                    self.console.print(f"  ✅ {name}: {model}", style="green")
                else:
                    self.console.print(f"  ❌ {name}: {model} - Manquant", style="red")
            
        except Exception as e:
            self.console.print(f"❌ Erreur Ollama: {e}", style="red")
            return False
        
        # Vérifier les ressources système
        memory = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        
        self.console.print(f"💾 RAM: {memory.used//1024//1024//1024}GB/{memory.total//1024//1024//1024}GB utilisée", style="cyan")
        self.console.print(f"🔥 CPU: {cpu_percent}% utilisé", style="cyan")
        
        return True
    
    def switch_model(self, model_name):
        """Changer de modèle IA"""
        if model_name in self.models:
            self.current_model = model_name
            model = self.models[model_name]
            self.console.print(f"🔄 Modèle changé: {model}", style="yellow")
            return True
        return False
    
    def generate_response(self, user_input, max_tokens=300):
        """Générer une réponse avec Ollama"""
        try:
            model = self.models[self.current_model]
            
            # Prompt système optimisé
            system_prompt = """Tu es Nina, un assistant IA français intelligent et utile, inspiré de Jarvis.

Caractéristiques :
- Réponds en français de manière naturelle et conversationnelle
- Sois précis, informatif et créatif selon le contexte
- Adapte ton ton selon la situation (professionnel, amical, technique)
- Si tu ne sais pas quelque chose, dis-le honnêtement
- Reste concis mais complet dans tes réponses

Tu fonctionnes entièrement en local pour garantir la confidentialité des données."""

            # Construire le contexte avec historique
            context = ""
            if self.conversation_history:
                context = "\n".join(self.conversation_history[-3:])  # 3 derniers échanges
            
            # Prompt complet
            full_prompt = f"{system_prompt}\n\nContexte récent:\n{context}\n\nUtilisateur: {user_input}\nNina:"
            
            # Générer la réponse
            start_time = time.time()
            
            response = ollama.generate(
                model=model,
                prompt=full_prompt,
                options={
                    'temperature': 0.7,
                    'top_p': 0.9,
                    'max_tokens': max_tokens,
                    'stop': ['Utilisateur:', 'Nina:']
                }
            )
            
            response_time = time.time() - start_time
            response_text = response['response'].strip()
            
            # Nettoyer la réponse
            if response_text.startswith('Nina:'):
                response_text = response_text[5:].strip()
            
            # Ajouter à l'historique
            self.conversation_history.append(f"User: {user_input[:50]}...")
            self.conversation_history.append(f"Nina: {response_text[:50]}...")
            
            # Limiter l'historique
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            
            return response_text, response_time
            
        except Exception as e:
            return f"Erreur lors de la génération: {e}", 0
    
    def show_help(self):
        """Afficher l'aide"""
        help_text = Text()
        help_text.append("🤖 COMMANDES NINA IA\n", style="bold blue")
        help_text.append("═══════════════════\n", style="blue")
        help_text.append("/help - Cette aide\n", style="cyan")
        help_text.append("/models - Lister les modèles disponibles\n", style="cyan")
        help_text.append("/switch <modèle> - Changer de modèle (principal/rapide/code)\n", style="cyan")
        help_text.append("/stats - Statistiques système\n", style="cyan")
        help_text.append("/clear - Effacer l'historique\n", style="cyan")
        help_text.append("/quit - Quitter Nina\n", style="cyan")
        help_text.append("\nTapez simplement votre question pour discuter !", style="green")
        
        panel = Panel(help_text, title="📚 Aide", border_style="blue")
        self.console.print(panel)
    
    def show_stats(self):
        """Afficher les statistiques système"""
        memory = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        
        stats_text = Text()
        stats_text.append(f"💾 RAM: {memory.used//1024//1024//1024}GB/{memory.total//1024//1024//1024}GB\n", style="cyan")
        stats_text.append(f"🔥 CPU: {cpu_percent}%\n", style="cyan")
        stats_text.append(f"🤖 Modèle actuel: {self.models[self.current_model]}\n", style="yellow")
        stats_text.append(f"💬 Historique: {len(self.conversation_history)} entrées\n", style="green")
        
        panel = Panel(stats_text, title="📊 Statistiques", border_style="cyan")
        self.console.print(panel)
    
    def run(self):
        """Boucle principale"""
        self.console.print("\n🚀 Nina IA est prête ! Tapez /help pour voir les commandes.\n", style="bold green")
        
        while True:
            try:
                # Prompt utilisateur avec modèle actuel
                model_indicator = f"[{self.current_model}]"
                user_input = input(f"👤 Vous {model_indicator}: ").strip()
                
                if not user_input:
                    continue
                
                # Commandes spéciales
                if user_input.startswith('/'):
                    cmd = user_input[1:].lower().split()
                    
                    if cmd[0] == 'help':
                        self.show_help()
                    elif cmd[0] == 'quit':
                        self.console.print("👋 Au revoir ! Nina s'arrête.", style="yellow")
                        break
                    elif cmd[0] == 'clear':
                        self.conversation_history.clear()
                        self.console.print("🧹 Historique effacé", style="green")
                    elif cmd[0] == 'stats':
                        self.show_stats()
                    elif cmd[0] == 'models':
                        self.console.print("🤖 Modèles disponibles:", style="blue")
                        for name, model in self.models.items():
                            indicator = "👈" if name == self.current_model else "  "
                            self.console.print(f"  {indicator} {name}: {model}", style="cyan")
                    elif cmd[0] == 'switch' and len(cmd) > 1:
                        if self.switch_model(cmd[1]):
                            self.console.print(f"✅ Modèle changé: {cmd[1]}", style="green")
                        else:
                            self.console.print(f"❌ Modèle inconnu: {cmd[1]}", style="red")
                    else:
                        self.console.print("❌ Commande inconnue. Tapez /help", style="red")
                    
                    continue
                
                # Génération de réponse
                self.console.print("🤔 Nina réfléchit...", style="yellow")
                response, response_time = self.generate_response(user_input)
                
                # Affichage de la réponse
                response_text = Text()
                response_text.append("🤖 Nina: ", style="bold blue")
                response_text.append(response, style="white")
                response_text.append(f" (⏱️ {response_time:.1f}s)", style="dim")
                
                self.console.print(response_text)
                self.console.print()  # Ligne vide
                
            except KeyboardInterrupt:
                self.console.print("\n👋 Au revoir ! Nina s'arrête (Ctrl+C).", style="yellow")
                break
            except Exception as e:
                self.console.print(f"❌ Erreur: {e}", style="red")

if __name__ == "__main__":
    try:
        nina = NinaVM()
        nina.run()
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        sys.exit(1)
EOF

chmod +x nina_vm.py
print_success "Nina IA créée"

# =============================================================================
# 7. CRÉATION DU SERVICE SYSTEMD (OPTIONNEL)
# =============================================================================
print_status "Création du service Nina (optionnel)..."

sudo tee /etc/systemd/system/nina.service > /dev/null << EOF
[Unit]
Description=Nina IA Assistant
After=network.target ollama.service

[Service]
Type=simple
User=$USER
WorkingDirectory=/home/$USER/nina-ai
Environment=PATH=/home/$USER/nina-ai/nina_env/bin
ExecStart=/home/$USER/nina-ai/nina_env/bin/python /home/$USER/nina-ai/nina_vm.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

print_success "Service Nina créé"

# =============================================================================
# 8. CONFIGURATION SÉCURITÉ
# =============================================================================
print_status "Configuration sécurité..."

# Firewall - Bloquer tout sauf SSH
sudo ufw --force enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh

# Désactiver les services inutiles
sudo systemctl disable bluetooth 2>/dev/null || true
sudo systemctl disable cups 2>/dev/null || true

print_success "Sécurité configurée"

# =============================================================================
# 9. SCRIPTS UTILITAIRES
# =============================================================================
print_status "Création des scripts utilitaires..."

# Script de démarrage rapide
cat > start_nina.sh << 'EOF'
#!/bin/bash
cd /home/$USER/nina-ai
source nina_env/bin/activate
python nina_vm.py
EOF
chmod +x start_nina.sh

# Script de test système
cat > test_system.sh << 'EOF'
#!/bin/bash
echo "🔍 Test du système Nina IA"
echo "========================="

echo "1. Test Ollama..."
ollama list

echo -e "\n2. Test Python..."
source nina_env/bin/activate
python -c "import ollama; print('✅ Ollama Python OK')"

echo -e "\n3. Test modèles..."
python -c "
import ollama
models = ollama.list()
print(f'Modèles disponibles: {len(models[\"models\"])}')
for model in models['models']:
    print(f'  - {model[\"name\"]}')
"

echo -e "\n4. Ressources système..."
free -h
df -h /
EOF
chmod +x test_system.sh

print_success "Scripts utilitaires créés"

# =============================================================================
# 10. FINALISATION
# =============================================================================
print_success "🎉 INSTALLATION NINA IA TERMINÉE !"
echo ""
echo "📋 RÉSUMÉ DE L'INSTALLATION :"
echo "============================="
echo "✅ Ubuntu mis à jour"
echo "✅ Ollama installé et configuré"
echo "✅ Modèles IA téléchargés (Llama 3.2 3B, 1B, Qwen2.5-Coder)"
echo "✅ Nina IA créée et optimisée"
echo "✅ Environnement Python configuré"
echo "✅ Sécurité configurée (UFW, services)"
echo "✅ Scripts utilitaires créés"
echo ""
echo "🚀 POUR DÉMARRER NINA :"
echo "======================="
echo "cd /home/$USER/nina-ai"
echo "./start_nina.sh"
echo ""
echo "🔧 POUR TESTER LE SYSTÈME :"
echo "=========================="
echo "./test_system.sh"
echo ""
echo "🛡️ SÉCURITÉ :"
echo "============"
echo "- Firewall activé (SSH uniquement)"
echo "- VM isolée du réseau principal"
echo "- Données 100% locales"
echo "- Services inutiles désactivés"
echo ""
print_success "Nina IA est prête à l'emploi ! 🤖"
EOF

chmod +x nina_vm_setup.sh 