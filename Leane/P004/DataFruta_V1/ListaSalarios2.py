import random
import numpy as np
from DataFruta_V1.analiseDados import AnaliseDados

class ListaSalarios2(AnaliseDados):
    
    def __init__(self, lista=None):
        super().__init__(type(float))
        if(lista.dtype == float):
            self.__lista = lista.copy()  
        else:
            self.__lista = np.zeros(0)
            
    @property
    def lista(self):
        return self.__lista.copy()
    
    #novos metodos estatisticos
            
    def calcularMediaGeometrica(self):
        produto = np.prod(self.__lista)
        mediaGeometrica = produto ** (1 / len(self.__lista))
        return mediaGeometrica
    
    
    def calcularMediaHarmonica(self):
        inversos = [1 / self.__lista]
        somaInversos = np.sum(inversos)
        mediaHarmonica = len(self.__lista) / somaInversos
        return mediaHarmonica
    
    
    def calculaMediaAritmetrica(self):
        media = self.__lista.mean()
        return media
    
    def calculaDesvioPadrao(self):
        desvioPadrao = self.__lista.std(ddof=1)
        return desvioPadrao
    
    def calculaVariancia(self):
        variancia = self.__lista.var(ddof=1)
        return variancia
    
    
    def geraListaSalario(n, SMin = 1320, SMax = 10000 ):
        listaSalarios2 = []
        for i in range(n):
            salario = random.uniform(SMin, SMax)
            listaSalarios2.append(salario)
        lista = ListaSalarios2(np.array(listaSalarios2))
        return lista 
    
    
    def addSalario(self):
        print("Informe o salário")
        salario = float(input())
        self.__lista.append(salario)
    
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
            resultado = ListaSalarios2.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana dos salários: {resultado}")   

    def mostraMenor(self):
        listaOrdenada = self.__lista.min()
        print(f"Menor salário: {listaOrdenada}")

    def mostraMaior(self):
        listaOrdenada = self.__lista.max()
        print(f"Maior salário: {listaOrdenada}") 
    
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
    
    def reajusteDezPorcento(self):
        for i in map((lambda s : s + s*0.1), self.__lista):
            print(i)