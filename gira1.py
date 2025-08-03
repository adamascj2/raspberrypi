import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

Ena = 3
In1 = 5
In2 = 7
try:
	GPIO.setup(Ena.GPIO.OUT)
	GPIO.setup(In1.GPIO.OUT)
	GPIO.setup(In2.GPIO.OUT)
	oPWM =GPIO.PWM(Ena,100)
	oPWM.start(0)

	oPWM.ChangeDutyCicle(60)
	GPIO.output(In1.GPIO(0)
	GPIO.output(In2.GPIO(1)
	time.sleep(10)
	oPWM.ChangeDutyCicle(0)
	time.sleep(2)
	oPWM.ChangeDutyCicle(30)
	GPIO.output(In1.GPIO(1)
	GPIO.output(In2.GPIO(0)
	time.sleep(10)
	oPWM.ChangeDutyCicle(0)

except KeyboardInterrupt:    # Ctrl c para interromper
	GPIO.cleanup()
        print('Tudo limpo')