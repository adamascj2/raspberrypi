import RPi.GPIO as GPIO
import time    
GPIO.setmode(GPIO.BOARD) 
pinoTRIG = 16
pinoECHO = 18
GPIO.setup(pinoTRIG,GPIO.OUT)
GPIO.setup(pinoECHO,GPIO.IN)

try:
    while True:
        GPIO.output(pinoTRIG,0)
        time.sleep(2E-6)        #2 mSeg
        GPIO.output(pinoTRIG,1)
        time.sleep(10E-6)       #10 mSeg
        GPIO.output(pinoTRIG,0)
        while GPIO.input(pinoECHO)==0:
            pass
        inicioT=time.time()
        while GPIO.input(pinoECHO)==1:
            pass
        fimT=time.time()
        T = fimT-inicioT
        print('T: ',T*1E6,' DISTANCIA: ',int(T*343/2*100 +0.5 ))

except KeyboardInterrupt:    # Ctrl c para interromper
    GPIO.cleanup()
    print('Tudo limpo')
