import tkinter as tk
from _buscaDados import BuscaDados
from _downloadDados import DownloadDados

class Interface:

    def __init__(self):
        self.busca = BuscaDados(anos=[], erro=None)
        self.down = DownloadDados()

    def interface(self):
        app = tk.Tk()
        app.title("Dados Meteorológicos")
        app.geometry('500x300')
        app.configure(background='#c38680')

        self.anos, self.erro = self.busca.buscaDados()

        if self.erro:
            mensagemErro = tk.Label(app, text=f"Erro ao obter dados: {self.erro}", background='#c38680', wraplength=450)
            mensagemErro.place(x=10, y=70, width=450, height=30)
        else:
            opcao = tk.StringVar(app)
            opcao.set(self.anos[0][0])
            texto1 = tk.OptionMenu(app, opcao, *[ano[0] for ano in self.anos],
                                    command=lambda anoSelecionado: self.down.downloadDados(anoSelecionado, self.anos))
            texto1.place(x=10, y=10, width=100, height=50)

        app.mainloop()
