#!/bin/bash

# 🤖 Nina AI - Script d'installation environnement Linux
# Auteur: Claude AI assistant
# Date: Janvier 2025

set -e  # Arrêter en cas d'erreur

echo "🤖 Installation environnement Nina AI pour Linux"
echo "================================================="

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction d'affichage coloré
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

# Vérification des prérequis
print_status "Vérification des prérequis système..."

# Vérifier Ubuntu
if ! lsb_release -d | grep -q "Ubuntu"; then
    print_warning "Ce script est optimisé pour Ubuntu. Continuez à vos risques."
fi

# Vérifier Python 3.10+
if ! python3 --version | grep -qE "Python 3\.(10|11|12)"; then
    print_error "Python 3.10+ requis. Votre version: $(python3 --version)"
    exit 1
fi

print_success "Prérequis système OK"

# Mise à jour du système
print_status "Mise à jour des packages système..."
sudo apt update && sudo apt upgrade -y

# Installation des dépendances système
print_status "Installation des dépendances système..."
sudo apt install -y \
    python3-pip \
    python3-venv \
    curl \
    wget \
    git \
    htop \
    tree \
    jq

# Création de l'environnement virtuel
print_status "Création de l'environnement virtuel Python..."
python3 -m venv nina_env
source nina_env/bin/activate

# Installation des packages Python
print_status "Installation des packages Python..."
pip install --upgrade pip
pip install \
    rich \
    psutil \
    requests \
    beautifulsoup4 \
    pyyaml \
    python-dateutil

# Installation d'Ollama
print_status "Installation d'Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.ai/install.sh | sh
    print_success "Ollama installé avec succès"
else
    print_warning "Ollama déjà installé"
fi

# Démarrage du service Ollama
print_status "Démarrage du service Ollama..."
sudo systemctl enable ollama
sudo systemctl start ollama

# Attendre que le service soit prêt
sleep 5

# Téléchargement des modèles IA
print_status "Téléchargement des modèles IA..."
print_warning "Cela peut prendre plusieurs minutes selon votre connexion..."

ollama pull llama3.2:1b
print_success "Modèle llama3.2:1b téléchargé (léger, rapide)"

ollama pull qwen2.5-coder:1.5b
print_success "Modèle qwen2.5-coder:1.5b téléchargé (code)"

# Optionnel: modèle plus gros si RAM suffisante
TOTAL_RAM=$(free -g | awk 'NR==2{print $2}')
if [ "$TOTAL_RAM" -gt 12 ]; then
    print_status "RAM suffisante détectée (${TOTAL_RAM}GB), téléchargement modèle avancé..."
    ollama pull llama3.2:3b
    print_success "Modèle llama3.2:3b téléchargé (avancé)"
else
    print_warning "RAM limitée (${TOTAL_RAM}GB), modèle 3B non téléchargé"
fi

# Création des dossiers de structure
print_status "Création de la structure de dossiers..."
mkdir -p src/{agents,utils}
mkdir -p config
mkdir -p docs
mkdir -p logs
mkdir -p cache
mkdir -p versions

# Déplacement des fichiers existants vers versions/
if [ -f "nina_text.py" ]; then
    mv nina_text.py versions/
    print_success "nina_text.py déplacé vers versions/"
fi

if [ -f "nina_advanced.py" ]; then
    mv nina_advanced.py versions/
    print_success "nina_advanced.py déplacé vers versions/"
fi

if [ -f "nina_fast.py" ]; then
    mv nina_fast.py versions/
    print_success "nina_fast.py déplacé vers versions/"
fi

# Test de fonctionnement Ollama
print_status "Test de fonctionnement d'Ollama..."
if ollama list | grep -q "llama3.2:1b"; then
    print_success "Ollama et modèles configurés correctement"
else
    print_error "Problème avec l'installation Ollama"
    exit 1
fi

# Affichage des informations système
print_status "Informations système:"
echo "  - OS: $(lsb_release -d | cut -f2)"
echo "  - Python: $(python3 --version)"
echo "  - RAM: ${TOTAL_RAM}GB"
echo "  - Modèles Ollama installés:"
ollama list | grep -E "(llama|qwen)" | sed 's/^/    /'

# Instructions finales
echo ""
print_success "🎉 Installation terminée avec succès !"
echo ""
echo "📋 Prochaines étapes:"
echo "  1. Activer l'environnement: source nina_env/bin/activate"
echo "  2. Lancer Nina AI: python src/nina_main.py"
echo "  3. Ouvrir Cursor AI pour développer"
echo ""
print_status "Nina AI est prête à être développée ! 🤖✨" 