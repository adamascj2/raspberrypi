 
from robot_hat import Ultrasonic, Pin
from robot_hat import Motors

us = Ultrasonic(Pin("D2"), Pin("D3"))
motors = Motors()
try:
	# Motor 1 clockwise at 20 speed
	motors[1].speed(20)
	# Motor 2  clockwise at 20% speed
	motors[2].speed(20)
	motors.forward(20)
 
	while True:
 		# Read distance
		distance = us.read()
		print(f"Distance: {distance}cm")
		if distance >= 5:
			# Stop all motors
			motors.stop()
			break

except KeyboardInterrupt:    # Ctrl c para interromper
	print('Encerrado')

 

 

