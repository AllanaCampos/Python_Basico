import random
from DataFruta_V1.analiseDados import AnaliseDados

class ListaSalarios(AnaliseDados):
    

    def __init__(self, lista = None):
        super().__init__(type(int))
        for i in lista:
            if type(i) != int:
                raise Exception("Tipo inválido para idade")
        self.__lista = lista.copy()      
        
        
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
    
    
    def geraListaSalario(n, SMin = 1320, SMax = 10000 ):
        listaSalarios = []
        for i in range(n):
            listaSalarios.append(random.randint(SMin, SMax))
        lista = ListaSalarios(listaSalarios)
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
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana dos salários: {resultado}")   

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor salário: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior salário: {listaOrdenada[listaOrdenada.__len__() - 1]}") 
    
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