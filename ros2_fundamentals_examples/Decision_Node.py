#! /usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DecisionNode(Node):
    def __init__(self):
        super().__init__('motor_decision')

        self.publisher_2 = self.create_publisher(String, '/motor_command', 10)

        self.subscriber_2 = self.create_subscription(
            String,
            '/motor_control',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')
        msg_out = String()

        value = float(msg.data)

        if value <= 30:
            msg_out.data = "STOP"

        self.publisher_2.publish(msg_out)
        self.get_logger().info(f'Data Sent Back to Main Node : "{msg_out.data}"')


def main(args=None):
    rclpy.init(args=args)

    minimal_py_subscriber2 = DecisionNode()

    rclpy.spin(minimal_py_subscriber2)

    minimal_py_subscriber2.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
