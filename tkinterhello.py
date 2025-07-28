import tkinter as tk

def print_hello():
    """
    Função chamada quando o botão é pressionado.
    Imprime "Hello World" no console.
    """
    print("Hello World")

# Cria a janela principal da aplicação Tkinter
app = tk.Tk()
app.title("Botão Hello World")
app.geometry("300x150") # Define o tamanho da janela

# Cria um rótulo (texto)
label = tk.Label(app, text="Clique no botão para ver a mensagem:", font=("Arial", 12))
label.pack(pady=20) # Adiciona o rótulo à janela com espaçamento

# Cria o botão
button = tk.Button(app, text="Diga Hello", command=print_hello, font=("Arial", 14), bg="lightblue")
button.pack(pady=10) # Adiciona o botão à janela com espaçamento

# Inicia o loop principal da aplicação Tkinter
app.mainloop()