from picarx import Picarx
import time


 
try:
    px = Picarx()
    px.forward(10)
    time.sleep(4)
    px.backward(10)
    time.sleep(4)
    px.forward(0)
         

except KeyboardInterrupt:    # Ctrl c para interromper
    px.forward(0)
    print('Encerrado')
