from DataFruta_V1 import  ListaSalarios, ListaIdades, ListaNomes, ListaDatas

def percorrerListas(nomes, salarios):
    for i in zip(nomes.lista, salarios.lista):
        print(i)


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    op = 0
    while(op != 8):
        print("<----------MENU---------->")
        print("1- Incluir um nome na lista de nomes")
        print("2- Incluir um salário na lista de salários")
        print("3- Incluir uma data na lista de datas")
        print("4- Incluir uma idade na lista de idades")
        print("5- Percorrer as listas de nomes e salários")
        print("6- Calcular o valor da folha com um reajuste de 10%")
        print("7- Modificar o dia das datas anteriores a 2019")
        print("8- Sair")
        op = int(input())

        match(op):
            case 1:
                nomes.addNome()
            case 2:
                salarios.addSalario()
            case 3:
                datas.addData()
            case 4:
                idades.addIdade()
            case 5:
                percorrerListas(nomes, salarios)
            case 6:
                salarios.reajusteDezPorcento()
            case 7:
                datas.modificaDataAnterior2019()


if __name__ == "__main__":
    main()