from ..resources import AnaliseDados
import numpy as np
import random
class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = None):
        super().__init__(type(int))
        if(lista.dtype == int):
            self.__lista = lista.copy()  
        else:
            self.__lista = np.zeros(0)
    
    @property
    def lista(self):
        return self.__lista.copy()
    
    def addIdade(self):
        print("Informe a idade")
        size = len(self.__lista)
        newLista = np.zeros(size+1)
        newLista[:-1] = self.__lista
        try:
            idade = int(input())
            self.__lista = newLista
            self.__lista[-1] = idade
        except Exception as e:
            print(e) 
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        self.__lista = np.zeros(qtd)
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite a idade {i+1}:")
                valor = int(input())
                self.__lista[i] = valor
        except Exception as e:
            print(e) 
    
    def mostraMediaAritmetica(self):
        return self.__lista.mean()

    def mostraMediaGeometrica(self):
        x = np.prod(self.__lista)
        return x ** (1/len(self.__lista))
    
    def mostraMediaHarmonica(self):
        x = 1/self.__lista
        x =  np.sum(x)
        return len(self.__lista)/x
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def mostraMedianaInferior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[int((listaOrdenada.__len__()/4)-1/2)]
            else:
                return ListaIdades.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()/4)-1/4)], listaOrdenada[int(listaOrdenada.__len__()/4)])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaIdades.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()//2)/2-1)], listaOrdenada[int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[int(listaOrdenada.__len__()//4)]
            
    def mostraMedianaSuperior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[-int((listaOrdenada.__len__()//4) + 1)]
            else:
                return ListaIdades.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//4))])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaIdades.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[-int((listaOrdenada.__len__()//4)+1)]

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

    def geraListaIdade(n, iMin = 18, iMax = 65):
        idades = [random.uniform(iMin, iMax) for _ in range(n)]
        lista = ListaIdades(np.array(idades))
        return lista
