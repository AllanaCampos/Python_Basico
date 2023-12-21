import random
from DataFruta_V1.analiseDados import AnaliseDados

class ListaNotas(AnaliseDados):
    

    def __init__(self, lista = None):
        super().__init__(type(float))
        for i in lista:
            if type(i) != float:
                raise Exception("Tipo inválido para notas")
        self.__lista = lista.copy()      
        
        
    @property
    def lista(self):
        return self.__lista.copy()
    
    
    def geraListaNotas(n, SMin = 0.0, SMax = 10.0 ):
        listaNotas = []
        for i in range(n):
            listaNotas.append(random.uniform(SMin, SMax))
        lista = ListaNotas(listaNotas)
        return lista 
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaNotas.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana dos salários: {resultado}")
        
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor salário: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior salário: {listaOrdenada[listaOrdenada.__len__() - 1]}")
        
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
    
    
    def calculaMediaAritmetrica(self):
        media = sum(self.__lista) / len(self.__lista)
        return media
    
    def calculaDesvioPadrao(self):
        mediaQuadrados = self.calculaVariancia()
        desvioPadrao = mediaQuadrados ** 0.5
        return desvioPadrao
    
    def calculaVariancia(self):
        media = self.calculaMediaAritmetrica()
        difQuadrados = [(i - media) ** 2 for i in self.__lista]
        mediaQuadrados = sum(difQuadrados) / len(difQuadrados)
        return mediaQuadrados
        
        
    def contarNotasAcimaDe(self, n):
        contador = 0
        for i in self.__lista:
            if i > n:
                contador += 1
        return contador
    
    def contarNotasAbaixoDe(self, n):
        contador = 0
        for i in self.__lista:
            if i < n:
                contador += 1
        return contador
    
    def adicionar1pontoAbaixoDe(self,n):
        notas = []
        for i in self._lista:
            if i < n:
                notas.append(i + 1)
            else:
                notas.append(i)
        lista = ListaNotas(notas)
        return lista
        
        
    