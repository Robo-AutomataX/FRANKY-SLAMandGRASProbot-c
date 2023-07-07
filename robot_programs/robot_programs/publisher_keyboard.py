#This node the keyboard preseed by the user and then published in a variable


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import tty
import termios

class KeyboardController(Node):

    def __init__(self):
        super().__init__('keyboard_controller')
        self.publisher_ = self.create_publisher(String, 'teclas_presionadas', 1)
        self.timer_ = self.create_timer(0.1, self.keyboard_callback)

    def keyboard_callback(self):
        key = self.getch()  # Obtener la tecla presionada
        msg = String()
        msg.data = key
        self.publisher_.publish(msg)  # Publicar la tecla en el topic
        print('Tecla presionada:', key)  # Imprimir la tecla en la terminal

    def getch(self):
        """Función para obtener la tecla presionada por el usuario"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def main(args=None):
    rclpy.init(args=args)
    keyboard_controller = KeyboardController()
    rclpy.spin(keyboard_controller)
    keyboard_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


