#! /usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
arduinoData = serial.Serial('/dev/ttyUSB0', 9600)


class SerialNode_Sub(Node):
    def __init__(self):
        super().__init__('led_node_serial')

        self.subscriber_1 = self.create_subscription(
            String,
            '/led_control',
            self.listener_callback,
            10)

        self.get_logger().info("Serial Node Initialized")

        while True:
            myCmd = input('please give your input : ')
            myCmd = myCmd + '\r'
            arduinoData.write(myCmd.encode())

    def listener_callback(self, msg):
        self.get_logger().info(f'Sending Command: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    serial_led_node = SerialNode_Sub()

    rclpy.spin(serial_led_node)

    serial_led_node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
