import rclpy
from rclpy.node import Node

class HelloRobot(Node):
    def __init__(self):
        super().__init__('hello_robot_node')
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.get_logger().info('Node Hello Robot démarré...')

    def timer_callback(self):
        self.get_logger().info('Hello ROS2!')

def main(args=None):
    rclpy.init(args=args)
    node = HelloRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
