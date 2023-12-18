from .analiseDados import AnaliseDados

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []  

    def addIdade(self):
        print("Informe a idade")
        idade = int(input())
        self.__lista.append(idade)
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a idade {i+1}:")
            valor = int(input())
            self.__lista.append(valor)
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana das idades: {resultado}")     
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor idade: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior idade: {listaOrdenada[listaOrdenada.__len__() - 1]}") 

    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media

