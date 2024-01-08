from .analiseDados import AnaliseDados
import random
import numpy as np

class ListaSalarios(AnaliseDados):

    def __init__(self, lista = []):
        super().__init__(type(float))
        self.__lista = np.array(lista) 
        
    def getLista(self):
        return self.__lista.copy()

    @property
    def lista(self):
        return self.__lista
    
    def addSalario(self):
        print("Informe o salário")
        salario = float(input())
        novaLista = self.getLista()
        self.__lista = np.zeros(novaLista.size + 1)
        self.__lista[:,-2]= novaLista
        self.__lista[-1] = salario   

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        self.__lista = np.zeros(qtd)
        for i in range(qtd):
            print(f"Digite o salário {i+1}:")
            valor = float(input())
            self.__lista[i] = valor

    def mostraMediana(self):
        mediana = np.median(self.__lista)
        return mediana    

    def mostraMenor(self):
        menor = np.min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = np.max(self.__lista)
        return maior
    
    def reajusteDezPorcento(self):
        self.__lista = self.__lista * 1.1
    
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
    
    def geraListaSalarios(n, sMin = 1320, sMax = 13200):
        listaSalariosAleatorios = [random.uniform(sMin, sMax) for _ in range(n)]
        return ListaSalarios(listaSalariosAleatorios)

    def calculaMediaAritmetica(self):
        mediaAritmetica = np.mean(self.__lista)
        return mediaAritmetica
        
    def medianaSuperior(self):
        dadosOrdenados = np.sort(self.__lista)
        n = len(dadosOrdenados)
        indiceMedianaSuperior = (n + 1) // 2
        medianaSuperior = dadosOrdenados[indiceMedianaSuperior - 1]
        return medianaSuperior
    
    def medianaInferior(self):
        dadosOrdenados = np.sort(self.__lista)
        n = len(dadosOrdenados)
        indiceMedianaInferior = n // 2
        medianaInferior = dadosOrdenados[indiceMedianaInferior - 1]
        return medianaInferior
    
    def mediaGeometrica(self):
        mediaGeometrica = np.prod(self.__lista) ** (1 / len(self.__lista))
        return mediaGeometrica

    def mediaHarmonica(self):
        mediaHarmonica = len(self.__lista) / np.sum(1 / np.array(self.__lista))
        return mediaHarmonica

    def desvioPadraoPopulacional(self):
        desvioPopulacional = np.std(self.__lista)
        return desvioPopulacional
    
    def varianciaPopulacional(self):
       varianciaPopulacional = np.var(self.__lista)
       return varianciaPopulacional
   
    def desvioPadraoAmostral(self):
        desvioAmostral = np.std(self.__lista, ddof=1)
        return desvioAmostral
    
    def varianciaAmostral(self):
        varianciaAmostral = np.var(self.__lista, ddof=1)
        return varianciaAmostral