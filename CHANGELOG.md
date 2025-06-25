# 📋 Changelog - Nina AI

Toutes les modifications importantes de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Ajouté
- Migration complète vers Linux Ubuntu
- Script d'installation automatique (`scripts/setup_env.sh`)
- Configuration Git et GitHub avec branches de développement
- Documentation complète du projet

## [0.3.0] - 2025-01-XX (Planifié - Linux)

### Ajouté
- Intégration Ollama avec modèles légers (llama3.2:1b, qwen2.5-coder:1.5b)
- Interface Rich colorée et moderne
- Architecture modulaire avec agents spécialisés
- Cache intelligent pour optimiser les performances
- Système de logs avancé
- Configuration YAML centralisée

### Modifié
- Migration complète de Windows vers Linux
- Optimisation des performances (objectif < 2 secondes)
- Structure de projet professionnelle

### Supprimé
- Dépendance GPT4All (remplacé par Ollama)
- Problèmes de performance Windows

## [0.2.0] - 2025-01-15 (Windows)

### Ajouté
- Version `nina_fast.py` avec agents spécialisés
- Cache intelligent pour les requêtes répétées
- Gestion d'erreurs robuste
- Interface colorée avec Rich

### Modifié
- Optimisation des temps de réponse
- Architecture modulaire améliorée

### Corrigé
- Problèmes de mémoire avec GPT4All
- Gestion des erreurs de modèles

## [0.1.0] - 2025-01-10 (Windows)

### Ajouté
- Version initiale `nina_text.py` fonctionnelle
- `nina_advanced.py` avec GPT4All Llama 3.2 3B
- `nina_simple.py` avec gestion audio basique
- Agents spécialisés : Général, Technique, Créatif, Recherche
- Documentation d'installation Windows

### Problèmes connus
- TTS Coqui incompatible sur Windows
- GPT4All très lent (6-11 secondes par réponse)
- DeepSeek-R1 incompatible

## [0.0.1] - 2025-01-05

### Ajouté
- Conception initiale du projet
- Recherche des technologies appropriées
- Configuration environnement de développement 