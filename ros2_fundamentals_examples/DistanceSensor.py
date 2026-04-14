#! /usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
arduinoData = serial.Serial('/dev/ttyUSB0', 9600)


class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_node_serial')

        self.publisher_1 = self.create_publisher(
            String, '/motor_control', 10)

        self.subscriber_1 = self.create_subscription(
            String,
            '/motor_command',
            self.listener_callback,
            10)

        # arduinoData.reset_input_buffer()
        self.get_logger().info("Serial Node Initialized")

        self.timer = self.create_timer(0.1, self.serial_read_data)

    def serial_read_data(self):
        msg = String()

        if arduinoData.in_waiting > 0:
            msg.data = arduinoData.readline().decode('utf-8').rstrip()
            self.publisher_1.publish(msg)
            self.get_logger().info(f'Motor Command: "{msg.data}"')


        # self.get_logger().info("Data recived")

    def listener_callback(self, msg_1):

        msg_2 = String()

        data = msg_1.data
        data = data + '\n'
        data = data.encode('utf-8')
        msg_2.data = data
        arduinoData.write(msg_2.data)
        self.get_logger().info(f'Motor Command: "{msg_2.data}"')


def main(args=None):
    rclpy.init(args=args)

    DistanceSensor_Node = DistanceSensor()

    rclpy.spin(DistanceSensor_Node)

    DistanceSensor_Node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
