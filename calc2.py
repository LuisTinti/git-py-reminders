import tkinter as tk

def clique_botao(valor):
    atual = visor.get()
    visor.set(atual + str(valor))

def limpar():
    visor.set("")

def calcular():
    try:
        resultado = eval(visor.get())
        visor.set(str(resultado))
    except Exception:
        visor.set("Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Máquina de números")
janela.geometry("400x300")
janela.config(bg="#ece3e3")
janela.resizable(True, True)

# Variável para armazenar o texto do visor
visor = tk.StringVar()

# Campo do Visor
entrada_visor = tk.Entry(
    janela, 
    textvariable=visor, 
    font=("Arial", 20), 
    bd=10, 
    insertwidth=2, 
    width=14, 
    borderwidth=4, 
    relief="ridge",
    justify="right"
)
entrada_visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Definição dos botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2),
]

# Criação e posicionamento dos botões numéricos e de operações básicas
for (texto, linha, coluna) in botoes:
    btn = tk.Button(
        janela, 
        text=texto, 
        font=("Arial", 14), 
        width=5, 
        height=2, 
        command=lambda t=texto: clique_botao(t)
    )
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de Limpar (C)
btn_limpar = tk.Button(
    janela, 
    text="C", 
    font=("Arial", 14), 
    width=5, 
    height=2, 
    bg="#ff6666", 
    fg="white", 
    command=limpar
)
btn_limpar.grid(row=4, column=3, padx=5, pady=5)

# Botão de Igual (=) ocupando duas colunas ou posicionado estrategicamente
btn_igual = tk.Button(
    janela, 
    text="=", 
    font=("Arial", 14), 
    width=23, 
    height=2, 
    bg="#66b3ff", 
    fg="white", 
    command=calcular
)
btn_igual.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Iniciar a aplicação
janela.mainloop()