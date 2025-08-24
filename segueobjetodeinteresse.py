from picarx import Picarx
from vilib import Vilib
import time

px = Picarx()

def clamp_number(num,a,b):
	return max(min(num, max(a, b)), min(a, b))

try:
   
    speed = 20
    dir_angle=0
    x_angle =0
    y_angle =0

    Vilib.camera_start()
    Vilib.display()
    Vilib.color_detect("red")

    while True:
        if Vilib.detect_obj_parameter['color_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['color_x']
            coordinate_y = Vilib.detect_obj_parameter['color_y']

            # muda angulo da camera para seguir objeto
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

            
            # muda angulo do servo-motor de esterçamento
             
            if dir_angle > x_angle:
                dir_angle -= 1
            elif dir_angle < x_angle:
                dir_angle += 1
            px.set_dir_servo_angle(x_angle)
            px.forward(speed)
            time.sleep(0.05)

        else :
            px.forward(0)
            time.sleep(0.05)


 
except KeyboardInterrupt:    # Ctrl c para interromper
	px.stop()
        print("Saindo")
        time.sleep(0.1)