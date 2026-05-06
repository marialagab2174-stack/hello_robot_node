from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='hello_robot_challenge', executable='hello_node', output='screen')
    ])
