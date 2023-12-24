from .analiseDados import AnaliseDados
from ._Datas import Data


class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def addData(self):
        print("Informe a data no seguinte formato: DD/MM/YYYY")
        data = input()
        dia = int(data.split(("/"))[0])
        mes = int(data.split(("/"))[1])
        ano = int(data.split(("/"))[2])
        data = Data(dia, mes, ano)
        self.__lista.append(data)

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de datas?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o a data {i + 1} no seguinte formato: DD/MM/YYYY")
            valor = input()
            dia = int(valor.split(("/"))[0])
            mes = int(valor.split(("/"))[1])
            ano = int(valor.split(("/"))[2])
            data = Data(dia, mes, ano)
            self.__lista.append(data)
    
    def mostraMediana(self):
        listaOrdenada = self.ordena()
        if listaOrdenada.__len__() % 2 == 0:
            pos = (listaOrdenada.__len__() // 2) -1
        else:
            pos = listaOrdenada.__len__() // 2
        print(f"Mediana das datas: {listaOrdenada[pos]}")    
     
    def mostraMenor(self):
        listaOrdenada = self.ordena()
        print(f"Primeira data: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = self.ordena()
        print(f"Última data: {listaOrdenada[listaOrdenada.__len__() - 1]}")
    
    def modificaDataAnterior2019(self):
        for i in filter((lambda d : Data(ano=2019).__gt__(d)), self.__lista):
            print(f"Deseja alterar o dia da data {i} para qual dia?")
            dia = int(input())
            i.dia = dia
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string

    def ordena(self):
        listaOrdenada = self.__lista.copy()
        for i in range(listaOrdenada.__len__()):
            for j in range(listaOrdenada.__len__() - i - 1):
                if(listaOrdenada[j].__gt__(listaOrdenada[j + 1])):
                    aux = listaOrdenada[j]
                    listaOrdenada[j] = listaOrdenada[j + 1]
                    listaOrdenada[j + 1] = aux
        return listaOrdenada