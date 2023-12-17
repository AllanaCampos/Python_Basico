from dataFruta import AnaliseDados

class ListaSalarios(AnaliseDados):
    

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        
        
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, valor):
        self.__lista = valor
        
        
    
    def addSalario(self):
        print("Informe o salário")
        salario = float(input())
        self.__lista.append(salario)
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        for i in listaOrdenada:
            print(str(i))
            

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o salário {i+1}:")
            valor = float(input())
            self.__lista.append(valor)

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