from .analiseDados import AnaliseDados
import random

class Notas(AnaliseDados):

    def __init__(self, lista = []):
        super().__init__(type(float))
        self.__lista = lista.copy() 
        
    def getLista(self):
        return self.__lista.copy()

    @property
    def lista(self):
        return self.__lista
    
    def addNota(self):
        print("Informe a nota")
        nota = float(input())
        self.__lista.append(nota)     

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de notas")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a nota {i+1}:")
            valor = float(input())
            self.__lista.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = Notas.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
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
    
    def geraListaNotas(n, nMin = 0, nMax = 10):
        listaNotasAleatorias = [random.uniform(nMin, nMax) for _ in range(n)]
        return Notas(listaNotasAleatorias)

    def calculaMediaAritmetica(self):
        mediaAritmetica = sum(self.__lista)/len(self.__lista)
        return mediaAritmetica
        
    def medianaSuperior(self):
        dadosOrdenados = sorted(self.__lista)
        n = len(dadosOrdenados)
        indiceMedianaSuperior = (n + 1) // 2
        medianaSuperior = dadosOrdenados[indiceMedianaSuperior]
        return medianaSuperior
    
    def medianaInferior(self):
        dadosOrdenados = sorted(self.__lista)
        n = len(dadosOrdenados)
        indiceMedianaInferior = n // 2
        medianaInferior = dadosOrdenados[indiceMedianaInferior - 1]
        return medianaInferior
    
    def mediaGeometrica(self):
        produto = 1.0
        n = len(self.__lista)
        for numero in self.__lista:
            produto *= numero
        mediaGeometrica = produto ** (1 / n)
        return mediaGeometrica

    def mediaHarmonica(self):
        soma = 0
        for numero in self.__lista:
            if numero == 0:
                raise ValueError("erro")
            soma += 1 / numero
        mediaHarmonica = len(self.__lista) / soma
        return mediaHarmonica

    def desvioPadraoPopulacional(self):
        somaQuadrados = sum((x - self.calculaMediaAritmetica()) ** 2 for x in self.__lista)
        desvio = (somaQuadrados/len(self.__lista)) ** (1/2)
        return desvio
    
    def varianciaPopulacional(self):
       varianciaPopulacio =  self.desvioPadraoPopulacional() ** 2
       return varianciaPopulacio
   
    def desvioPadraoAmostral(self):
        somaQuadrados = sum((x - self.calculaMediaAritmetica()) ** 2 for x in self.__lista)
        desvio = (somaQuadrados/(len(self.__lista) -1)) ** (1/2)
        return desvio
    
    def varianciaAmostral(self):
        varianciaAmostra =  self.desvioPadraoAmostral() ** 2
        return varianciaAmostra
    
    def moda(self):
        frequencias = {}
        for nota in self.__lista:
            if nota in frequencias:
                frequencias[nota] += 1
            else:
                frequencias[nota] = 1

        modaValor = max (frequencias, key = frequencias.get)
        modaContagem = frequencias[modaValor]
        modas = [valor for valor, contagem in frequencias.items() if contagem == modaContagem]
        return modas