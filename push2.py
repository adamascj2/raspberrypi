import time    
import RPi.GPIO as GPIO    
GPIO.setmode(GPIO.BOARD)   
pinoBotao=13                 
pinoLED=11                   
GPIO.setup(pinoBotao,GPIO.IN,pull_up_down=GPIO.PUD_UP)  
GPIO.setup(pinoLED,GPIO.OUT)
estado=1 
estadoAnterior=1
estadoLED=0
try: 
	while True: 
		estado = GPIO.input(pinoBotao)  # Verifica se estado é 1 ou 0    	
         	print(estado)
		if estado==1 and estadoAnterior==0
			estadoLED=not estadoLED  #Inverte o estadoLED
              		GPIO.output(pinoLED,estadoLED)
		estadoAnterior=estado  
             	time.sleep(.5)

except KeyboardInterrupt:    # Ctrl c para interromper
	GPIO.cleanup()
        print('Tudo limpo')