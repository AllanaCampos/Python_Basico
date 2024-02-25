from .app import *
from .manipulacaoDeDados import *
from .analiseDeDados import *

def main():
    dados = ManipulacaoDeDados()
    app = App()
    app.setAnos(dados.getDados())
    print("\n\n")
    app.mainloop()

if __name__ == "__main__":
    main()