import rclpy
import psutil
from rclpy.node import Node
from std_msgs.msg import Float32


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Float32, "cpu_usage", 10)
        self.create_timer(0.5, self.cb)


    def cb(self):
        msg = ()
        msg.data = psutil.cpu_percent(interval=1)
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
