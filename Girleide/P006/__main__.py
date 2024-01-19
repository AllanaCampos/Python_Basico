import Restic as rt
import pandas as pd

def main():
    residente = rt.Residente()
    trilha = rt.Trilha()

    while True:
        print("--------MENU---------")
        print("1 - adicionar um novo residente")
        print("2 - visualizar dados por trilhas")
        print("3 - visualizar todos os dados")
        print("4 - Encerrar")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            residente.dadosResidente()
        elif opcao == '2':
            trilha.escolhaTrilha(residente)
        elif opcao == '3':
            pass
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
