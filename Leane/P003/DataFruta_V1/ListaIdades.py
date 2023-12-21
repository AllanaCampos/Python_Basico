import random
from DataFruta_V1.analiseDados import AnaliseDados

class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = None):
        super().__init__(type(int))
        for i in lista:
            if type(i) != int:
                raise Exception("Tipo inválido para idade")
        self.__lista = lista .copy() 
         
        
    @property
    def lista(self):
        return self.__lista.copy()    
    
    
    #novos metodos estatisticos
    
            
    def calcularMediaGeometrica(self):
        produto = 1
        for i in self.__lista:
            produto *= i
        mediaGeometrica = produto ** (1 / len(self.__lista))
        return mediaGeometrica
    
    
    def calcularMediaHarmonica(self):
        inversos = [1 / x for x in self.__lista]
        somaInversos = sum(inversos)
        mediaHarmonica = len(self.__lista) / somaInversos
        return mediaHarmonica
    
    
    def calculaMediaAritimetrica(self):
        media = sum(self.__lista) / len(self.__lista)
        return media
    
    def calculaDesvioPadrao(self,media):
        difQuadrados = [(i - media) ** 2 for i in self.__lista]
        mediaQuadrados = sum(difQuadrados) / len(difQuadrados)
        desvioPadrao = mediaQuadrados ** 0.5
        return desvioPadrao 
    
    def calculaVariancia(self,media,difQuadrados):
        variancia = sum(difQuadrados) / len(difQuadrados)
        return variancia
    
    
    def geraListaIdade(n, IMin = 18, IMax = 65 ):
        listaIdades = []
        for i in range(n):
            listaIdades.append(random.randint(IMin, IMax))
        lista = ListaIdades(listaIdades)
        return lista 
    
    def addIdade(self):
        print("Informe a idade")
        idade = int(input())
        self.__lista.append(idade)
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        for i in listaOrdenada:
            print(str(i))

    
    def entradaDeDados(self):
        print("Quantos elementos deseja gerar?")
        n = int(input())
        return n
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado   
        
    
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