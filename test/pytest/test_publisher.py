#!/usr/bin/env python3


"""
test suite for verfifying the functionality of minimal ros2 publisher
"""
import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher


def test_publisher_creation():
    # Initialize ros2
    rclpy.init()

    try:
        # create a instance of publisher

        node = MinimalPyPublisher()

        # Test1 : Verify the node name is correct
        assert node.get_name() == "minimal_py_publisher"

        # Test2  -  Verify pub exists and correct topic name
        assert hasattr(node, 'publisher_1')
        assert node.publisher_1.topic_name == '/py_example_topic'

    finally:

        rclpy.shutdown()


def test_message_counter():

    # check if counter increases properly
   # Initialize ros2
    rclpy.init()

    try:
        # create a instance of publisher

        node = MinimalPyPublisher()

        # create variable for of counter
        initial_count = node.i

        # call timer function
        node.timer_callback()

        # check the counter increment
        assert node.i == initial_count + 1

    finally:

        rclpy.shutdown()


def test_ContentMessage():
    # Initialize ros2
    rclpy.init()

    try:
        # create a instance of publisher
        node = MinimalPyPublisher()

        node.i = 5

        msg = String()

        msg.data = f'Hello World: {node.i}'

        assert msg.data == 'Hello World: 5'

    finally:

        rclpy.shutdown()


if __name__ == '__main__':
    pytest.main(['-v'])
