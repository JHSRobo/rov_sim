import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from core.msg import Float32Arr
from math import copysign

class DepthSensor(Node):
    def __init__(self):
        super().__init__('depth_sensor')

        self.depth = 0
        self.vert_vel = 0

        # Quick reference for logging
        self.log = self.get_logger()

        # Define publishers and subscribers
        self.thruster_sub = self.create_subscription(Float32Arr, 'thrusters', self.thruster_callback, 10)
        self.depth_pub = self.create_publisher(Float32, 'depth', 10)

        # Timer, to periodically publish depth data
        self.timer = self.create_timer(0.2, self.timer_callback)

    def timer_callback(self):
        self.depth_pub.publish

    def thruster_callback(self, t_vals):
        cutoff = 0.25 # Speed below this threshold is negligible

        # Dampen velocity over time. If it's close enough to 0, set it to 0
        if abs(self.vert_vel) >= cutoff:
            self.vert_vel = copysign(abs(self.vert_vel) - cutoff, self.vert_vel)
        else:
            self.vert_vel = 0

        # Add thruster value to the velocity and change depth by vel
        vert_thrust = (t_vals.array[4] + t_vals.array[5]) / 2
        self.vert_vel -= vert_thrust
        self.depth += self.vert_vel / 100.

        if self.depth < 0: 
            self.depth = 0.0
            if self.vert_vel > 0: self.vert_vel = 0.0

        # Wrap and publish the depth
        depth_msg = Float32()
        depth_msg.data = round(self.depth, 2)
        self.depth_pub.publish(depth_msg)


def main():
    rclpy.init()

    depth = DepthSensor()

    # Runs the program until shutdown is recieved
    rclpy.spin(depth)

    # On shutdown, kill node
    depth.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

