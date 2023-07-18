# This publisher read the information of the sensor and then calculate the
# distance and different information and then published in a variable



import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import serial
import time
import math

class MinimalPublisher(Node):
    interface_luna = serial.Serial('/dev/serial0',115200)

    def __init__(self,frame_id):
        super().__init__('minimal_publisher')

        self.ser_motores = serial.Serial('/dev/ttyACM1',115200)
        self.publisher_ = self.create_publisher(LaserScan, 'lidar_publisher', 10)
        timer_period = 0.001  # seconds
        luna_enableOutput  = [0x5a,0x05,0x07,0x01,0x00]

        self.scan = LaserScan()
        self.contador = 1
        self.aux = 0
        #self.scan.header.frame_id = 'map'
        #self.scan.range_min = 0.0 #Distancia mínima que puede medir
        #self.scan.range_max = 8.0 #Distancia máxima que puede medir
        #self.scan.angle_max = math.pi #Ángulo máximo (media vuelta)
        #self.scan.angle_min = 0.0 #Ángulo mínimo (cero grados)
        #self.scan.angle_increment = math.pi/1024.0 #El angulo que barre en 1024 pasos

        #self.scan.scan_time = 10.288484  #Tiempo total del escaneo
        #self.scan.ranges = self.distances
        #self.publisher_publisher(self.scan)

        self.distances = []

        #self.scan.angle_min = -1.57  # -90 grados
        #self.scan.angle_max = 1.57  # 90 grados
        #self.scan.angle_increment = 0.01  # Incremento de ángulo pequeño para mayor resolución
        #self.scan.time_increment = 0.0  # No se necesita incremento de tiempo en este caso
        #self.scan.scan_time = 0.1  # Tiempo total de escaneo
        #self.scan.range_min = 0.0  # Distancia mínima de detección
        #self.scan.range_max = 10.0  # Dis



        if self.interface_luna.isOpen() :
            self.get_logger().info("TF-Luna sucessfully opened")
            self.interface_luna.write(luna_enableOutput)
            time.sleep(0.5)
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0

        else :
            self.get_logger().info("could not open TF-Luna, won't publish anything.")


    def timer_callback(self):
        counter = self.interface_luna.in_waiting
        bytes_to_read = 9
        if counter > bytes_to_read-1:
            bytes_serial = self.interface_luna.read(bytes_to_read) 
            self.interface_luna.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes

                #self.scan.data = 'Distance: %d cm' % distance
                #   f"Strength: {strength:2.0f} / 65535 (16-bit), "
                #   f"Chip Temperature: {temperature:2.1f} C")
                #self.publisher_.publish(scan)
                #self.get_logger().info('Publishing: "%s"' % distance)

                if self.ser_motores.in_waiting>0:
                    pass
                    #print(self.ser_motores.readline().decode('utf-8'))



                #self.scan.header.frame_id = 'map'
                #self.scan.angle_min = 0.0
                #self.scan.angle_max = math.pi
                #self.scan.angle_increment = math.pi /4
                #self.scan.range_min = 0.0
                #self.scan.range_max = 7.0
                #self.scan.time_increment = 1.0  # No se necesita incremento de tiempo en este c>
                #self.scan.scan_time = 4.0  # Tiempo total de escaneo

                #self.scan.ranges = [4.0,4.0,4.0,4.0]

                #self.publisher_.publish(self.scan)





                if self.ser_motores.in_waiting > 0:
                    serial_variable = self.ser_motores.readline().decode('utf-8')

                    distance = float(distance)/100.0

                    print("Paso: "+ serial_variable +" distancia: " +  str(distance))
                    self.distances.append(distance)
                    if len(self.distances)==1024:

                        if self.aux == 1:
                           self.distances.reverse()
                           self.aux = 0
                        elif self.aux == 0:
                           self.aux = 1


                        self.scan.header.frame_id = 'map'
                        self.scan.range_min = 0.0 #Distancia mínima que puede medir
                        self.scan.range_max = 8.0 #Distancia máxima que puede medir
                        self.scan.angle_max = math.pi #Ángulo máximo (media vuelta)
                        self.scan.angle_min = 0.0 #Ángulo mínimo (cero grados)
                        self.scan.angle_increment = math.pi/1024.0 #El angulo que barre en 1024 pasos

                        self.scan.scan_time = 10.288484  #Tiempo total del escaneo
                        self.scan.ranges = self.distances
                        self.publisher_.publish(self.scan)


                        print(self.distances)
                        self.distances = []




def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher(frame_id = "map")

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()