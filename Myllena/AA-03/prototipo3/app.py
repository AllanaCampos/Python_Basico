import tkinter as tk
import shutil
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .coletaDados import ColetaDados
from .scrollableFrame import ScrollableFrame
from .verificacaoDeDados import VerificacaoDeDados


class App(tk.Tk):
  
    # Classe que representa a interface do programa
    
    def __init__(self):
        super().__init__()

        
        self.title("Prototipo 03")
        self._path = "./climaplotDonwloads/"
        self._ano = tk.StringVar()


        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_close(self):
        
        #  Metódo que deleta a pasta de donwloads e tudo contido nela
        
        
        print("\n\n\nFinalizando Programa...")
        print("\nExcluindo donwloads...")

        try:
            shutil.rmtree(self._path)
            print(f"\nDonwloads excluidos com sucesso!")
        except OSError as e:
            print(f"\nErro ao excluir a pasta: {e}!")
        
        self.quit()

    def setGraficos(self,estacao):
        canvas = FigureCanvasTkAgg(
            VerificacaoDeDados.plotGrafico(
                estacao["path"]), 
                master=self)

        canvas.draw()
        canvas.get_tk_widget().grid(
            column=2,
            row=0,
            sticky="ns",padx=0)
        
    
    def botaoEstacaoClick(self,estacao):
        self.setGraficos(estacao)


    def setEstacoes(self,estacoes):
        j=0
        estacoesFrame = ScrollableFrame(self)
        estacoesFrame.grid(
            column=1, 
            row=0, 
            sticky="nsew")

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
                text="ANOS DISPONÍVEIS:",
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
                     text="Sem conexão",
                     bg="Yellow",
                     font=("DejaVu Sans", 16,"bold")
                     ).grid(column=0,
                            row=i,
                            sticky="ew",
                            pady=3)
        


