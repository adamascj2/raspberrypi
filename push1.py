import time    
import RPi.GPIO as GPIO    
GPIO.setmode(GPIO.BOARD)   
pinoBotao=13                 
pinoLED=11                   
GPIO.setup(pinoBotao,GPIO.IN,pull_up_down=GPIO.PUD_UP)  
GPIO.setup(pinoLED,GPIO.OUT)
circuitoAberto=1 
try: 
	while True: 
        	circuitoAberto = GPIO.input(pinoBotao)  # Verifica se circuito aberto ou nao      	
         	print(circuitoAberto)
		if circuitoAberto==1:
              		GPIO.output(pinoLED,0)  
                if circuitoAberto==0:        # Botao apertado!
              		GPIO.output(pinoLED,1)  
           	time.sleep(.5)

except KeyboardInterrupt:    # Ctrl c para interromper
	GPIO.cleanup()
        print('Tudo limpo')