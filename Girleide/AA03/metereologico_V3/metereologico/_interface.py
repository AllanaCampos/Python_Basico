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
            mensagemErro.place(x=10, y=70, width=450, height=100)
        else:
            opcao = tk.StringVar(app)
            opcao.set("ANO")
            texto1 = tk.OptionMenu(app, opcao, *[ano[0] for ano in self.anos],
                                    command=lambda anoSelecionado: self.escolhaCidades(anoSelecionado, app))
            texto1.place(x=10, y=10, width=100, height=50)
        app.mainloop()


    def escolhaCidades(self, anoSelecionado, app):
        self.cidades = self.down.downloadDados(anoSelecionado, self.anos)
        opcao2 = tk.StringVar(app)
        opcao2.set("CIDADE")
        texto2 = tk.OptionMenu(app, opcao2, *self.cidades)
        texto2.place(x=10, y=70, width=150, height=50)
