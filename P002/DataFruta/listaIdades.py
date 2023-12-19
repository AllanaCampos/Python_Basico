from DataFruta import AnaliseDados
import random
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
    
    def addIdade(self):
        print("Informe a idade")
        try:
            idade = int(input())
            self.__lista.append(idade)
        except Exception as e:
            print(e) 
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite a idade {i+1}:")
                valor = int(input())
                self.__lista.append(valor)
        except Exception as e:
            print(e) 
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]

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
        idades = []
        for i in range(n):
            idades.append(random.randint(iMin, iMax))
        lista = ListaIdades(idades)
        return lista
