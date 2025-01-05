#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch cpu_usage_ros2 talk_listen.launch.py | tee -i /tmp/cpu_usage_ros2.log

cat /tmp/cpu_usage_ros2.log |
