 
from robot_hat import Ultrasonic, Pin
from robot_hat import Motor

try:

	us = Ultrasonic(Pin("D2"), Pin("D3"))
	mE = Motor(id=1,dir=0)
	mD = Motor(id=2,dir=0)
	mE.set_power(20)
	mD.set_power(20)

 
	while True:
 		# Read distance
		distance = us.read()
		print(f"Distance: {distance}cm")
		if distance <= 5:
			# Stop all motors
			mE.set_power(0)
			mD.set_power(0)
			break

except KeyboardInterrupt:    # Ctrl c para interromper
	print('Encerrado')

 

 

