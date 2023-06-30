#! /usr/bin/env python 3

import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist



class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10 ) #tipo de mensaje, el nombre
        self.timer = self.create_timer(0.5,self.send_velocity_command)  # llama a la funcion cada 0.5segundos
        self.get_logger().info("Draw circle node has been started")

    def send_velocity_command(self):
        msg = Twist() #crea un mensaje para luego enviarlo
        msg.linear.x = 2.0 # establece valores para las variables dentro del msg
        msg.angular.z = 1.0

        self.cmd_vel_pub_.publish(msg) #publica el mensaje msg




def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()








if __name__ == "main":
    main()
