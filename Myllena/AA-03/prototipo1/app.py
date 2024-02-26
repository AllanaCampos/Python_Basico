import tkinter as tk
from .scrollableFrame import ScrollableFrame

class App(tk.Tk):
    """
        Classe que representa a interface do programa
    """
    def __init__(self):
        super().__init__()

        
        self.title("Prototipo 01")


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)




    def botaoAnoClick(self,anoLink):
        print(f"ano: {anoLink['ano']}, link: {anoLink['link']}")

    
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
                    bg="Green",
                    font=("DejaVu Sans", 12, "bold")
                ).grid(
                    column=0,
                    row=i,
                    sticky="ew",
                    pady=3)


        else:
            tk.Label(master=anosFrame.scrollableFrame,
                     text="Sem conexão",
                     bg="Blue",
                     font=("DejaVu Sans", 16,"bold")
                     ).grid(column=0,
                            row=i,
                            sticky="ew",
                            pady=3)

