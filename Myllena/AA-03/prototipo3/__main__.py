from .app import App
from .coletaDados import ColetaDados
from .verificacaoDeDados import VerificacaoDeDados

def main ():
    dados = ColetaDados()
    app = App()
    app.setAnos(dados.getDados())
    app.mainloop()
    
if __name__ == "__main__":
    main()