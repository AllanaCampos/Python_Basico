import random
from dataFruta.analiseDados import AnaliseDados

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