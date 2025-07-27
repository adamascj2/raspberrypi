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
DC=2  #Duty cycle
oPWM = GPIO.PWM(pinoLED,1000)   #Como se ligasse em forma de pulso com frequencia acima de 60 hertz/seg
oPWM.start(DC)

try:
	while True:	
  
		estado = GPIO.input(pinoBotao)  # Verifica se estado é 1 ou 0    	
         	print(estado)
		if estado==1 and estadoAnterior==0
			DC=DC+10
     			print('DC: '+DC)
			print('Brilhando mais')
		if DC>99:
			DC=2
		oPWM.ChangeDutyCycle(DC)
		estadoAnterior=estado
             	time.sleep(.5)

except KeyboardInterrupt:    # Ctrl c para interromper
        oPWM.stop()
	GPIO.cleanup()
        print('Tudo limpo')