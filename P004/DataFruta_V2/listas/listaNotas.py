from ..resources import AnaliseDados
import numpy as np
import random
class ListaNotas(AnaliseDados):

    def __init__(self, lista=None):
        super().__init__(type(float))
        if(lista.dtype == float):
            self.__lista = lista.copy()  
        else:
            self.__lista = np.zeros(0)

    @property
    def lista(self):
        return self.__lista.copy()
    
    def addNota(self):
        print("Informe a nota")
        size = len(self.__lista)
        newLista = np.zeros(size+1)
        newLista[:-1] = self.__lista
        try:
            nota = float(input())
            self.__lista = newLista
            self.__lista[-1] = nota
        except Exception as e:
            print(e)        

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de notas?")
        qtd = int(input())
        self.__lista = np.zeros(qtd)
        try:
            for i in range(qtd):
                print(f"Digite a nota {i+1}:")
                valor = float(input())
                self.__lista[i] = valor
        except Exception as e:
            print(e) 

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaNotas.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado 

    def mostraMedianaInferior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[int((listaOrdenada.__len__()/4)-1/2)]
            else:
                return ListaNotas.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()/4)-1/4)], listaOrdenada[int(listaOrdenada.__len__()/4)])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaNotas.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()//2)/2-1)], listaOrdenada[int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[int(listaOrdenada.__len__()//4)]
            
    def mostraMedianaSuperior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[-int((listaOrdenada.__len__()//4) + 1)]
            else:
                return ListaNotas.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//4))])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaNotas.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[-int((listaOrdenada.__len__()//4)+1)]

    def mostraMediaAritmetica(self):
        return self.__lista.mean()

    def mostraMediaGeometrica(self):
        x = np.prod(self.__lista)
        return x ** (1/len(self.__lista))
    
    def mostraMediaHarmonica(self):
        x = 1/self.__lista
        x =  np.sum(x)
        return len(self.__lista)/x
    
    def mostraDesvioPadraoPopulacional(self):
        return self.__lista.std(ddof=0)
    
    def mostraDesvioPadraoAmostral(self):
        return self.__lista.std(ddof=1)
    
    def mostraVarianciaPopulacional(self):
        return self.__lista.var(ddof=0)
    
    def mostraVarianciaAmostral(self):
        return self.__lista.var(ddof=1)
    
    def mostraMenor(self):
        return self.__lista.min()

    def mostraMaior(self):
        return self.__lista.max()
    
    def reajusteDezPorcento(self):
        for i in map((lambda s : s + s*0.1), self.__lista):
            print(i)
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        for i in listaOrdenada:
            print(str(i))
    
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

    def geraListaNotas(n, iMin = 0, iMax = 10):
        notas = [random.uniform(iMin, iMax) for _ in range(n)] 
        lista = ListaNotas(np.array(notas))
        return lista

    def adicionaPonto(self, n):
        self.__lista += n
        for i in self.__lista:
            if i > 10:
                i = 10

    def maiorQue(self, n):
        filtro = self.__lista > n
        maior = self.__lista[filtro]
        return maior
    
    def menorQue(self, n):
        filtro = self.__lista < n
        menor = self.__lista[filtro]
        return menor

    def aprovados(self, media):
        filtro = self.__lista >= media
        aprovados = self.__lista[filtro]
        return aprovados

    def reprovados(self, media):
        filtro = self.__lista < media
        reprovados = self.__lista[filtro]
        return reprovados
    
    def passarMaiorNotaPara10(self):
        nota = self.mostraMaior()
        self.__lista = (self.__lista * 10) / nota

