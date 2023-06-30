#!usr/bin/env python3


import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        
        self.counter = 0
        super().__init__("first_node") #it is name that will appear in graph
        self.create_timer(1.0, self.timer_callback) #timer que llama a timer.callback cada 1 segundo
   
    def timer_callback(self):
         self.get_logger().info("Hello " + str(self.counter)) 
         self.counter +=1


def main(args=None):
      
    rclpy.init(args=args) #Inicia la comunicación con ros 2
    node = Mynode() #Instancia un objeto de la clase Mynode
    

    rclpy.spin(node) #Como un while que repite el nodo y no permite que termine hasta hace ctrl + c
    rclpy.shutdown() #Finaliza la comunicación con ros 2


if __name__ == "__main__":
      main()