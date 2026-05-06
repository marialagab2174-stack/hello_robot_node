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

## 🧠 Fonctionnalités Autonomes
Ce projet inclut désormais un nœud de conduite autonome basé sur les données du Lidar :
- **Obstacle Avoidance** : Le robot s'arrête et pivote si un objet est détecté à moins d'un mètre.
- **Gazebo Integration** : Utilise les plugins `libgazebo_ros_diff_drive.so` pour le mouvement.

## 🚀 Lancement
1. Lancer la simulation :
   ```bash
   ros2 launch miniproject_3_autonomous_drive_robot display.launch.py
   ```
2. Lancer l'autonomie :
   ```bash
   python3 src/miniproject_3_autonomous_drive_robot/scripts/autonomous_drive.py
   ```
