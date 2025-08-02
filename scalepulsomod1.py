import tkinter as tk
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pinoLED=11                   
GPIO.setup(pinoLED,GPIO.OUT) 
GPIO.output(pinoLED,0)
oPWM = GPIO.PWM(pinoLED,1000)   #Como se ligasse em forma de pulso com frequencia acima de 60 hertz/seg
DC=0   #Definição da variavel com valor do Dutycycle
oPWM.start(DC)

def mostrarbrilho():
	valor_selecionado = escala_dc.get()
        label_resultado.config(text=f"DC selecionado: {valor_selecionado}")
        oPWM.ChangeDutyCycle(int(valor_selecionado))	
	time.sleep(.5)
try:

	app = tk.Tk()
	app.title("Controle de DC")
	app.geometry("400x250") 
	label_instrucao = tk.Label(app, text="Mova o controle para ajustar o valor de DC:", font=("Arial", 12))
	label_instrucao.pack(pady=15)
 	escala_dc = tk.Scale(
    		app,
    		from_=0,
    		to=100,
    		orient=tk.HORIZONTAL,
    		length=300,
    		resolution=1,
    		font=("Arial", 10)
	)
	escala_dc.set(0) # Define o valor inicial para 0
	escala_dc.pack(pady=10)
	botao_projetar = tk.Button(
    		app,
    		text="Mostrar brilho",
    		command=mostrarbrilho,
    		font=("Arial", 12),
    		bg="lightgreen"
	)
	botao_projetar.pack(pady=15)
	label_resultado = tk.Label(app, text="DC selecionado: ", font=("Arial", 14), fg="blue")
	label_resultado.pack(pady=10)
	app.mainloop()
													
except KeyboardInterrupt:    # Ctrl c para interromper
	GPIO.cleanup()

        print('Tudo limpo')

