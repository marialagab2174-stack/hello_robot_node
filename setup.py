from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hello_robot_challenge'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maria Lagab',
    description='CHALLENGE SYNTAXE: Hello Robot ROS2',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'hello_node = hello_robot_challenge.hello_node:main'
        ],
    },
)
