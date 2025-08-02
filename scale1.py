import tkinter as tk

def exibir_valor():
    """
    Função chamada quando o botão é pressionado.
    Obtém o valor do Scale e o exibe no Label.
    """
    # Obtém o valor atual do controle Scale
    valor_selecionado = escala_dc.get()
    # Atualiza o texto do Label com o valor selecionado
    label_resultado.config(text=f"DC selecionado: {valor_selecionado}")

# Cria a janela principal da aplicação Tkinter
app = tk.Tk()
app.title("Controle de DC")
app.geometry("400x250") # Define um tamanho um pouco maior para a janela

# Rótulo de instrução
label_instrucao = tk.Label(app, text="Mova o controle para ajustar o valor de DC:", font=("Arial", 12))
label_instrucao.pack(pady=15)

# Cria o controle Scale (deslizante)
# from_=-40 e to=40 definem o intervalo
# orient=tk.HORIZONTAL define a orientação
# length define o comprimento em pixels
# resolution define o incremento (1 significa que avança de 1 em 1)
escala_dc = tk.Scale(
    app,
    from_=-40,
    to=40,
    orient=tk.HORIZONTAL,
    length=300,
    resolution=1,
    font=("Arial", 10)
)
escala_dc.set(0) # Define o valor inicial para 0
escala_dc.pack(pady=10)

# Botão para projetar o valor no label
botao_projetar = tk.Button(
    app,
    text="Mostrar Valor DC",
    command=exibir_valor,
    font=("Arial", 12),
    bg="lightgreen"
)
botao_projetar.pack(pady=15)

# Rótulo onde o valor selecionado será exibido
label_resultado = tk.Label(app, text="DC selecionado: ", font=("Arial", 14), fg="blue")
label_resultado.pack(pady=10)

# Inicia o loop principal da aplicação Tkinter
app.mainloop()