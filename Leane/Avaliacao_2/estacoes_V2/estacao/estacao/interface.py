import tkinter as tk
from dados import BuscaDados
from obtencaoDados import ObterDados

class Interface:
    
    def __init__(self):
        self.ano = BuscaDados([], erros = None)
        self.dados = ObterDados()
    
    def interface(self):
        app = tk.Tk()
        app.title("Dados Meteorológicos")
        app.geometry('500x300')
        app.configure(background='#c38680')
        
        anos, erros = self.ano.obter_anos_disponiveis()  #atribuir valores retornados pela função
        self.anos = anos  # Atribuir anos à instância da classe

        if self.anos:
            opcao = tk.StringVar(app)
            opcao.set(self.anos[0][0])
            texto = tk.OptionMenu(app, opcao, *[ano[0] for ano in self.anos],
                command=lambda anoSelecionado: self.escolhaCidades(anoSelecionado, app))
            texto.place(x=10, y=10, width=100, height=50)
        else:
            mensagemErro = tk.Label(app, text=f"Erro ao obter dados: {erros}", background='#c38680', wraplength=450)
            mensagemErro.place(x=10, y=70, width=450, height=30)

        app.mainloop()
    
    def escolhaCidades(self, anoSelecionado, app):
        self.cidades = self.dados.downloadDados(anoSelecionado, self.anos)
        opcao2 = tk.StringVar(app)
        opcao2.set("CIDADE")
        texto2 = tk.OptionMenu(app, opcao2, *self.cidades)
        texto2.place(x=10, y=70, width=150, height=50)