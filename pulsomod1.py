import time    
import RPi.GPIO as GPIO    
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(pinoLED,GPIO.OUT)
oPWM = GPIO.PWM(pinoLED,1000)   #Como se ligasse em forma de pulso com frequencia acima de 60 hertz/seg
pinoLED=11
DC=0
oPWM.start(DC)

try:
	while True:	
		for DC in range (0,99,5):
			oPWM.ChangeDutyCycle(DC)	
			time.sleep(.5)
		for DC in range (0,99,-5):
			oPWM.ChangeDutyCycle(DC)	
			time.sleep(.5)


except KeyboardInterrupt:    # Ctrl c para interromper
        oPWM.stop()
	GPIO.cleanup()
        print('Tudo limpo')