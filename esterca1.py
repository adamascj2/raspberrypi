from robot_hat import Servo
import time
try:
    
	sv = Servo('P2') #No P2 está o servomotor de esterçamento
	sv.angle(40)
	time.sleep(5)
	sv.angle(-40)
	time.sleep(5)
	sv.angle(0)
 


except KeyboardInterrupt:    # Ctrl c para interromper
	 print('Encerrado')
