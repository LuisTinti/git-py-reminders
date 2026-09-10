import tkinter as tk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.root.geometry("600x400")
        self.root.configure(bg="#2c3e50")
        
        # Variáveis de controle de tempo
        self.tempo_decorrido = 0
        self.rodando = False
        self.processo_id = None
        
        # Elemento de texto do cronômetro
        self.label_tempo = tk.Label(
            root, text="00:00:00", font=("Times New Roman", 36, "bold"), 
            bg="#2c3e50", fg="#ecf0f1"
        )
        self.label_tempo.pack(pady=30)
        
        # Container para os botões
        self.frame_botoes = tk.Frame(root, bg="#2c3e50")
        self.frame_botoes.pack()
        
        # Configuração dos botões
        self.botao_iniciar = tk.Button(
            self.frame_botoes, text="Iniciar", command=self.iniciar, 
            font=("Times New Roman", 10, "bold"), bg="#2ecc71", fg="white", width=8
        )
        self.botao_iniciar.grid(row=0, column=0, padx=5)
        
        self.botao_pausar = tk.Button(
            self.frame_botoes, text="Pausar", command=self.pausar, 
            font=("Times New Roman", 10, "bold"), bg="#f1c40f", fg="white", width=8
        )
        self.botao_pausar.grid(row=0, column=1, padx=5)
        
        self.botao_zerar = tk.Button(
            self.frame_botoes, text="Zerar", command=self.zerar, 
            font=("Times New Roman", 10, "bold"), bg="#e74c3c", fg="white", width=8
        )
        self.botao_zerar.grid(row=0, column=2, padx=5)

    def atualizar_tempo(self):
        if self.rodando:
            self.tempo_decorrido += 1
            
            # Formata o tempo em HH:MM:SS
            horas = self.tempo_decorrido // 3600
            minutos = (self.tempo_decorrido % 3600) // 60
            segundos = self.tempo_decorrido % 60
            
            string_tempo = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.label_tempo.config(text=string_tempo)
            
            # Chama esta mesma função novamente após 1000 milissegundos (1 segundo)
            self.processo_id = self.root.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()

    def pausar(self):
        if self.rodando:
            self.root.after_cancel(self.processo_id)
            self.rodando = False

    def zerar(self):
        if self.rodando:
            self.root.after_cancel(self.processo_id)
            self.rodando = False
        self.tempo_decorrido = 0
        self.label_tempo.config(text="00:00:00")

# Inicialização do aplicativo
if __name__ == "__main__":
    janela = tk.Tk()
    app = Cronometro(janela)
    janela.mainloop()
