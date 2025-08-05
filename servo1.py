import RPi.GPIO as GPIO
import time    
GPIO.setmode(GPIO.BOARD)   
pinoPWM=12
GPIO.setup(pinoPWM,GPIO.OUT)
oPWM = GPIO.PWM(pinoPWM,50)   #Tem que ser 50 hertz/seg
DC=0   #Definição da variavel com valor do Dutycycle
oPWM.start(DC)

try:
    while True:
        DC = float (input('Entre com um DC entre 4 e 10 ')) #7 é horizontal
        oPWM.ChangeDutyCycle(DC)	
        time.sleep(3)
         
except KeyboardInterrupt:    # Ctrl c para interromper
    oPWM.stop()
    GPIO.cleanup()
    print('Tudo limpo')
