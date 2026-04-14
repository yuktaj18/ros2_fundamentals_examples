#!/bin/bash

cleanup(){

  echo "Restarting ROS 2 daemon to cleanup before shutting down"
  ros2 daemon stop
  sleep 1
  ros2 daemon start
  echo "Terminating all ROS2 related process.."
  kill 0
  exit


}

trap 'cleanup' SIGINT

ros2 run ros2_fundamentals_examples py_minimal_publisher.py &

sleep 2

ros2 run ros2_fundamentals_examples py_minimal_subscriber.py

