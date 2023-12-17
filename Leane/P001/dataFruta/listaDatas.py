from dataFruta import Data, AnaliseDados 

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []  
        
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, valor):
        self.__lista = valor
        
        
    
    def addData(self):
        print("Informe a data no seguinte formato: DD/MM/YYYY")
        data = input()
        dia = int(data.split(("/"))[0])
        mes = int(data.split(("/"))[1])
        ano = int(data.split(("/"))[2])
        data = Data(dia, mes, ano)
        self.__lista.append(data)
    
    
    def ordenaLista(self):
        listaOrdenada = self.__lista.copy()  
        while True:
            Troca = False
            for i in range(len(listaOrdenada) - 1):
                if listaOrdenada[i].__gt__(listaOrdenada[i + 1]):
                    Troca = True
                    listaOrdenada[i], listaOrdenada[i + 1] = listaOrdenada[i + 1], listaOrdenada[i]
            if not Troca:
                break
        return listaOrdenada
    
    
    
    def listarEmOrdem(self):
        listaOrdenada = self.ordenaLista()
        for i in listaOrdenada:
            print(i)
    
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
        listaOrdenada = self.ordenaLista()
        if listaOrdenada.__len__() % 2 == 0:
            pos = (listaOrdenada.__len__() // 2) -1
        else:
            pos = listaOrdenada.__len__() // 2
        print(f"Mediana das datas: {listaOrdenada[pos]}")    
     
    def mostraMenor(self):
        listaOrdenada = self.ordenaLista()
        print(f"Primeira data: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = self.ordenaLista()
        print(f"Última data: {listaOrdenada[listaOrdenada.__len__() - 1]}")
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string