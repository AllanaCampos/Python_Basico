from ..resources import AnaliseDados
import random
class ListaSalarios(AnaliseDados):

    def __init__(self, lista=None):
        super().__init__(type(float))
        if(lista != None):
            for i in lista:
                if type(i) != float:
                    raise Exception("Tipo inválido para salário")
            self.__lista = lista.copy()  
        else:
            self.__lista = []

    @property
    def lista(self):
        return self.__lista.copy()
    
    def addSalario(self):
        print("Informe o salário")
        try:
            salario = float(input())
            self.__lista.append(salario)
        except Exception as e:
            print(e)      

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite o salário {i+1}:")
                valor = float(input())
                self.__lista.append(valor)
        except Exception as e:
            print(e) 

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado 
    
    def mostraMedianaInferior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[int((listaOrdenada.__len__()/4)-1/2)]
            else:
                return ListaSalarios.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()/4)-1/4)], listaOrdenada[int(listaOrdenada.__len__()/4)])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaSalarios.calculaMedia(listaOrdenada[int((listaOrdenada.__len__()//2)/2-1)], listaOrdenada[int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[int(listaOrdenada.__len__()//4)]
            
    def mostraMedianaSuperior(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            if ((listaOrdenada.__len__()//2)-1) % 2 == 0:
                return listaOrdenada[-int((listaOrdenada.__len__()//4) + 1)]
            else:
                return ListaSalarios.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//4))])
        else:
            if (listaOrdenada.__len__()//2) % 2 == 0:
                return ListaSalarios.calculaMedia(listaOrdenada[-int((listaOrdenada.__len__()//2)/2+1)], listaOrdenada[-int((listaOrdenada.__len__()//2)/2)])
            else:
                return listaOrdenada[-int((listaOrdenada.__len__()//4)+1)]

    def mostraMediaAritmetica(self):
        x = sum(self.__lista)
        return x/len(self.__lista)

    def mostraMediaGeometrica(self):
        x = 1
        for i in self.__lista:
            x *= i
        return x ** (1/len(self.__lista))
    
    def mostraMediaHarmonica(self):
        x = 0
        for i in self.__lista:
            x += 1/i
        return len(self.__lista)/x
    
    def mostraDesvioPadraoPopulacional(self):
        variancia = self.mostraVarianciaPopulacional()
        return variancia ** 1/2
    
    def mostraDesvioPadraoAmostral(self):
        variancia = self.mostraVarianciaAmostral()
        return variancia ** 1/2
    
    def mostraVarianciaPopulacional(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista))
    
    def mostraVarianciaAmostral(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/(len(self.__lista) - 1))
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]
    
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

    def geraListaSalario(n, iMin = 1320, iMax = 13200):
        salarios = []
        for i in range(n):
            salarios.append(random.uniform(iMin, iMax))
        lista = ListaSalarios(salarios)
        return lista