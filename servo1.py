import RPi.GPIO as GPIO
import time    
GPIO.setmode(GPIO.BOARD)   
pinoPWM=12
GPIO.setup(pinoPWM,GPIO.OUT)
oPWM = GPIO.PWM(pinoLED,50)   #Tem que ser 50 hertz/seg
DC=0   #Definição da variavel com valor do Dutycycle
oPWM.start(DC)

try:
	while True:
       		DC = float('Entre com um DC entre 0 e 15: ')	
		oPWM.ChangeDutyCycle(DC)	
		time.sleep(3)
		 
except KeyboardInterrupt:    # Ctrl c para interromper
        oPWM.stop()
	GPIO.cleanup()
        print('Tudo limpo')