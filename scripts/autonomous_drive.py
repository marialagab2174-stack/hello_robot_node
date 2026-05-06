import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class AutonomousDrive(Node):
    def __init__(self):
        super().__init__('autonomous_drive_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.move_cmd = Twist()

    def lidar_callback(self, msg):
        # On regarde la distance devant le robot (index central du Lidar)
        front_distance = msg.ranges[len(msg.ranges)//2]

        if front_distance < 1.0: # Si obstacle à moins de 1m
            self.get_logger().warn('Obstacle détecté ! Tourne...')
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.5
        else:
            self.get_logger().info('Chemin libre. Avance...')
            self.move_cmd.linear.x = 0.3
            self.move_cmd.angular.z = 0.0
        
        self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousDrive()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
