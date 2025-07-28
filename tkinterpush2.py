import tkinter as tk
import time    
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BOARD)
pinoLED=11                   
GPIO.setup(pinoLED,GPIO.OUT)   
def acende():
	GPIO.output(pinoLED,1)
	time.sleep(.5)
def apaga():
	GPIO.output(pinoLED,0)
	time.sleep(.5)

try:
	
	# Cria a janela principal da aplicação Tkinter
	app = tk.Tk()
	app.title("LIGA/DESLIGA")
	app.geometry("400x250") # Define o tamanho da janela

	# Cria um rótulo (texto)
	label = tk.Label(app, text="Clique no botão para acender/apagar o LED:", font=("Arial", 12))
	label.pack(pady=20) # Adiciona o rótulo à janela com espaçamento

	# Cria o botão1
	button1 = tk.Button(app, text="ACENDER", command=acende, font=("Arial", 14), bg="lightblue")
	button1.pack(pady=10) # Adiciona o botão à janela com espaçamento
	# Cria o botão2
	button2 = tk.Button(app, text="APAGAR", command=apaga, font=("Arial", 14), bg="lightblue")
	button1.pack(pady=10) # Adiciona o botão à janela com espaçamento

	# Inicia o loop principal da aplicação Tkinter
	app.mainloop()

except KeyboardInterrupt:    # Ctrl c para interromper
		GPIO.cleanup()
        	print('Tudo limpo'