# 🤖 Nina AI - Assistant Vocal Intelligent

> Assistant IA vocal type Jarvis, 100% local, optimisé pour Linux

## 📋 Vue d'ensemble

**Nina AI** est un assistant vocal intelligent conçu pour fonctionner entièrement en local, sans dépendance aux services cloud. Le projet a été migré de Windows vers Linux pour une meilleure performance et un environnement de développement optimal.

## 🎯 Objectifs du projet

- 🗣️ **Assistant vocal** naturel et intelligent
- 🧠 **IA 100% locale** - Aucune donnée envoyée sur internet
- 🎨 **Interface colorée** et moderne
- ⚡ **Performance optimisée** pour environnement Linux
- 🔧 **Développement fluide** avec Cursor AI

## 🏗️ Architecture

```
nina-ai/
├── 📁 src/                    # Code source principal
│   ├── nina_main.py          # Interface principale
│   ├── agents/               # Agents IA spécialisés
│   │   ├── math_agent.py     # Calculs mathématiques
│   │   ├── time_agent.py     # Gestion du temps
│   │   ├── creative_agent.py # Réponses créatives
│   │   └── general_agent.py  # Agent général
│   └── utils/                # Utilitaires
│       ├── cache.py          # Système de cache
│       ├── monitoring.py     # Monitoring système
│       └── voice.py          # Gestion audio
├── 📁 config/                # Configuration
│   ├── models.yaml          # Configuration modèles IA
│   └── settings.yaml        # Paramètres application
├── 📁 docs/                  # Documentation
│   ├── MIGRATION_GUIDE.md   # Guide de migration
│   └── LINUX_SETUP.md      # Installation Linux
├── 📁 scripts/              # Scripts utilitaires
│   ├── install_ollama.sh   # Installation Ollama
│   └── setup_env.sh        # Configuration environnement
└── 📁 versions/             # Versions précédentes
    ├── nina_text.py         # Version texte simple
    ├── nina_advanced.py     # Version GPT4All
    └── nina_fast.py         # Version avec cache
```

## 🚀 Installation rapide (Linux)

```bash
# 1. Cloner le projet
git clone https://github.com/VOTRE_USERNAME/nina-ai.git
cd nina-ai

# 2. Exécuter l'installation automatique
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh

# 3. Lancer Nina AI
python src/nina_main.py
```

## 🔧 Prérequis

### Système Linux (Ubuntu 22.04+ recommandé)
- Python 3.10+
- 16GB RAM (recommandé)
- Ollama pour les modèles IA
- Cursor AI pour le développement

### Modèles IA recommandés
- `llama3.2:3b` - Modèle principal (réactif)
- `qwen2.5-coder:1.5b` - Assistance code
- `llama3.2:1b` - Modèle léger (backup)

## 📊 Historique de développement

### ✅ Versions Windows (terminées)
- **nina_text.py** - Version texte fonctionnelle
- **nina_advanced.py** - GPT4All Llama 3.2 3B (lent: 6-11s)
- **nina_fast.py** - Agents spécialisés + cache intelligent

### 🎯 Version Linux (en cours)
- **nina_main.py** - Version optimisée avec Ollama
- Interface colorée avec Rich
- Monitoring temps réel
- Performance maximisée

## 🔄 Migration Windows → Linux

Le projet a été migré vers Linux pour :
- 🚀 **Performance IA** - Ollama optimisé pour Ubuntu
- 🛠️ **Développement** - Environnement natif Linux
- 🔧 **Stabilité** - Pas de conflits Windows/antivirus
- 📈 **Évolutivité** - Base solide pour fonctionnalités futures

## 🎨 Fonctionnalités

### Interface utilisateur
- 🌈 Interface colorée avec animations
- 📊 Monitoring système en temps réel
- 💬 Conversations naturelles
- 📝 Historique intelligent

### Capacités IA
- 🧮 Calculs mathématiques
- ⏰ Gestion du temps et dates
- 🎭 Réponses créatives et blagues
- 💡 Conseils et support émotionnel
- 🔍 Recherche et information

## ⚡ Performance

### Optimisations
- 💾 **Cache intelligent** - Réponses instantanées pour questions courantes
- 🤖 **Agents spécialisés** - Répartition intelligente des tâches
- 🧠 **Modèles légers** - Équilibre performance/qualité
- 📊 **Monitoring** - Surveillance ressources en temps réel

### Ressources VM
- 💻 **RAM allouée** : 16GB
- 🖥️ **OS** : Ubuntu 22.04.5 LTS + XFCE
- 🔧 **Outils** : VMware Tools, Cursor AI, Terminator

## 📚 Documentation

- [Guide Migration](docs/MIGRATION_GUIDE.md) - Contexte complet de migration
- [Installation Linux](docs/LINUX_SETUP.md) - Configuration environnement
- [API Agents](docs/API.md) - Documentation des agents IA

## 🤝 Contribution

Ce projet est développé avec l'assistance de Claude AI via Cursor AI pour un développement optimal et une architecture robuste.

## 📄 Licence

Projet personnel - Usage libre pour apprentissage et développement.

---

**🎯 Prochaine étape :** Installation Ollama + Développement nina_main.py optimisé 