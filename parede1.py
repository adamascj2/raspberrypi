 
from robot_hat import Ultrasonic, Pin
from robot_hat import Motor, PWM, Pin
us = Ultrasonic(Pin("D2"), Pin("D3"))
motor = Motor(PWM("P13"), Pin("D4"))try:
	 
	motor.speed(20)
	 
 
	while True:
 		# Read distance
		distance = us.read()
		print(f"Distance: {distance}cm")
		if distance >= 5:
			# Stop all motors
			motor.speed(0)

			break

except KeyboardInterrupt:    # Ctrl c para interromper
	print('Encerrado')

 

 

