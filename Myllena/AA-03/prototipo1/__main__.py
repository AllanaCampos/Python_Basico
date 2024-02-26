from .app import App
from .coletaDados import ColetaDados

def main():
    dados = ColetaDados()
    app = App()
    app.setAnos(dados.getDados())
    print("\n\n")
    app.mainloop()

if __name__ == "__main__":
    main()