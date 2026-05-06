# CHALLENGE SYNTAXE : Hello Robot! 🤖

## Description
Ce projet consiste à créer un nœud ROS 2 (Python) capable de loguer un message de bienvenue à intervalle régulier.

## 🎯 Objectifs du Challenge
- Créer un nœud nommé `hello_robot_node`.
- Implémenter un timer déclenché toutes les **2.0 secondes**.
- Afficher le message **'Hello ROS2!'** via le logger standard.

## 🏗 Structure du Package
- **hello_robot_challenge/** : Cœur du code source.
- **launch/** : Script de démarrage automatisé.
- **resource/** : Fichiers d'indexation pour `colcon`.
- **test/** : Tests de conformité (PEP8/Flake8).

## 🚀 Utilisation
```bash
# Compilation
cd ~/ros2_ws
colcon build --packages-select hello_robot_challenge
source install/setup.bash

# Lancer via le fichier Launch
ros2 launch hello_robot_challenge hello_launch.py
```

---
**Maria Lagab** - *Spécialité Robotique et Système Intelligent*
