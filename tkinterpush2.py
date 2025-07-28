import tkinter as tk
def acende():
	import time    
	import RPi.GPIO as GPIO    
	GPIO.setmode(GPIO.BOARD)   
    	pinoLED=11                   
	GPIO.setup(pinoLED,GPIO.OUT)
	estado=1 
	estadoAnterior=1
	estadoLED=0
	try: 
		while True: 
			print(estado)
			if estado==1 and estadoAnterior==0
				estadoLED=not estadoLED  #Inverte o estadoLED
              			GPIO.output(pinoLED,estadoLED)
				estadoAnterior=estado  
             		time.sleep(.5)

	except KeyboardInterrupt:    # Ctrl c para interromper
		GPIO.cleanup()
        	print('Tudo limpo'
# Cria a janela principal da aplicação Tkinter
app = tk.Tk()
app.title("PushButton")
app.geometry("300x150") # Define o tamanho da janela

# Cria um rótulo (texto)
label = tk.Label(app, text="Clique no botão para acender/apagar o LED:", font=("Arial", 12))
label.pack(pady=20) # Adiciona o rótulo à janela com espaçamento

# Cria o botão
button = tk.Button(app, text="ACENDER/APAGAR", command=acende, font=("Arial", 14), bg="lightblue")
button.pack(pady=10) # Adiciona o botão à janela com espaçamento

# Inicia o loop principal da aplicação Tkinter
app.mainloop()