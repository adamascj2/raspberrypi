import RPi.GPIO as gpio
import time
continuar = 'S'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while continuar == 'S'
	piscadas = int(input('Quantas piscadas vc deseja? :'))
	for i range(0,piscadas)
		GPIO.output(11,ON)
		time.sleep(1)
		GPIO.output(11,OFF)
		time.sleep(1)
	continuar = input('Quer continuar testando? (S para SIM):')
GPIO.cleanup()

               