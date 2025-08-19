from pydoc import text
from vilib import Vilib
from time import sleep, time, strftime, localtime
import threading
import readchar
import os

 
flag_color = False
 

manual = '''
Entre com tecla para função
    q: Tirar foto
    1: Encontar objetos da cor: red
    2: orange
    3: yellow
    4: green
    5: blue
    6: purple
    0: Desligar detecção
     
     
'''

color_list = ['close', 'red', 'orange', 'yellow',
        'green', 'blue', 'purple',
]

 


 

def take_photo():
    _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
    name = 'photo_%s'%_time
    username = os.getlogin()

    path = f"/home/{username}/Pictures/"
    Vilib.take_photo(name, path)
    print('foto salva como %s%s.jpg'%(path,name))


def object_show():
    global flag_color 

    if flag_color is True:
        if Vilib.detect_obj_parameter['color_n'] == 0:
            print('Color Detect: None')
        else:
            color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
            color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
            print("[Cor da pesquisa] ","Coordinate:",color_coodinate,"Size",color_size)

     
def main():
    global   flag_color 
     

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    print(manual)

    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # take photo
        if key == 'q':
            take_photo()
        # color detect
        elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
            index = int(key)
            if index == 0:
                flag_color = False
                Vilib.color_detect('close')
            else:
                flag_color = True
                Vilib.color_detect(color_list[index]) # color_detect(color:str -> color_name/close)
            print('Cor da pesquisa : %s'%color_list[index])
        
        
        

        sleep(0.5)


if __name__ == "__main__":
    main()
