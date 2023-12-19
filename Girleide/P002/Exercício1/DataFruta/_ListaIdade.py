from .analiseDados import AnaliseDados
import random

class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = []):
        super().__init__(type(int))
        self.__lista = lista.copy() 
        
    def getLista(self): 
        return self.__lista.copy()

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
        return resultado   
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]

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

    def geraListaIdades(n, iMin = 18, iMax = 65):
        listaIdadesAleatorias = [random.randint(iMin, iMax) for _ in range(n)]
        return ListaIdades(listaIdadesAleatorias)
