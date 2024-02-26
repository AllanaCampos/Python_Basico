import tkinter as tk
import shutil
from .scrollableFrame import ScrollableFrame
from .coletaDados import ColetaDados

# CLASSE QUE REPRESENTA A INTERFACE DO PROGRAMA
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        
        self.title("Prototipo 02")
        self._path = "./pototipo2Donwloads/"
        self._ano = tk.StringVar()


        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

# METODO PARA DELETAR A PASTA DE DONWLOAD COMPLETA ASSIM QUE A APLICAÇÃO FOR FECHADA
    def on_close(self):
        
        print("\n\n\nFinalizando Programa...")
        print("\nExcluindo donwloads...")

        try:
            shutil.rmtree(self._path)
            print(f"\nDonwloads excluidos com sucesso!")
        except OSError as e:
            print(f"\nErro ao excluir a pasta: {e}!")
        
        self.quit()

# FUNÇÃO QUE PEGA A ESTAÇÃO ESTAÇÃO E O CAMINHO CSV CORRESPONDENTE  
    def botaoEstacaoClick(self,estacao):
        print(f"\nestação: {estacao['estação']}, caminho do csv: {estacao['path']}")


    def setEstacoes(self,estacoes):
        j=0
        estacoesFrame = ScrollableFrame(self)
        estacoesFrame.grid(column=1, row=0, sticky="nsew")

        tk.Label(
            master=estacoesFrame.scrollableFrame,
            text= f"ESTAÇÕES DISPONíVEIS PARA {self._ano.get()} :",
            bg="Thistle",
            font=("DejaVu Sans", 16,"bold")
        ).grid(
            column=0,
            row=j,
            sticky="ew",
            pady=3)

        for estacao in estacoes:
            j+=1
            tk.Button(
                master=estacoesFrame.scrollableFrame,
                text=estacao["estação"],
                bg="Orange",
                command= (lambda estacao=estacao: self.botaoEstacaoClick(estacao)),
                font=("DejaVu Sans", 12, "bold")
            ).grid(
                column=0,
                row=j,
                sticky="ew",
                pady=3)

# FUNÇÃO QUE FAZ O DONWLOAD DO CSV QUE SERÁ ADICIONADO NO BOTÃO
    def botaoAnoClick(self,anoLink):
        ColetaDados.donwloadCSV(anoLink,self._path)
        self._ano.set(anoLink["ano"])
        estacoes = ColetaDados.getEstacoes(self._ano.get(),self._path)
        self.setEstacoes(estacoes)

    
    def setAnos(self,anosLinks):
        i=0
        anosFrame = ScrollableFrame(self)
        anosFrame.grid(column=0, row=i, sticky="nsew")
        if len(anosLinks)>0:

            tk.Label(
                master=anosFrame.scrollableFrame,
                text="ANOS DISPONíVEIS:",
                bg="Thistle",
                font=("DejaVu Sans", 16,"bold")
            ).grid(
                column=0,
                row=i,
                sticky="ew",
                pady=3)

            for anoLink in anosLinks:
                i+=1

                tk.Button(
                    master=anosFrame.scrollableFrame,
                    text=anoLink["ano"],
                    command=(lambda anoLink=anoLink: self.botaoAnoClick(anoLink)),
                    bg="Orange",
                    font=("DejaVu Sans", 12, "bold")
                ).grid(
                    column=0,
                    row=i,
                    sticky="ew",
                    pady=3)


        else:
            tk.Label(master=anosFrame.scrollableFrame,
                     text="Falha na conexão",
                     bg="Salmon",
                     font=("DejaVu Sans", 16,"bold")
                     ).grid(column=0,
                            row=i,
                            sticky="ew",
                            pady=3)