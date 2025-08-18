from picarx import Picarx
import time
import readchar

texto = '''
Use as teclas
    w: Frente
    s: Tras
    a: Virar a esquerda
    d: Virar a direita
    ctrl+c: Sair
'''

def titulo():
    print("\033[H\033[J",end='')  # para limpar a tela
    print(texto)

try:
       
        px = Picarx()
        titulo()
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    px.set_dir_servo_angle(0)
                    px.forward(20)
                elif 's' == key:
                    px.set_dir_servo_angle(0)
                    px.backward(20)
                elif 'a' == key:
                    px.set_dir_servo_angle(-35)
                    px.forward(20)
                elif 'd' == key:
                    px.set_dir_servo_angle(35)
                    px.forward(20)
                 
                 
                titulo()
                time.sleep(0.5)
                px.forward(0)

            elif key == readchar.key.CTRL_C:
                print("\n Sair")
                break

    except KeyboardInterrupt:    # Ctrl c para interromper
     	px.set_dir_servo_angle(0)
        px.stop()
        time.sleep(.2)