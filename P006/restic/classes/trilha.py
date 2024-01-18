import pandas as pd
class Trilha:
    def __init__(self, nome, id):
        self.__index = id
        self.__residentes = pd.DataFrame([])
        self.__nome = nome
    
    def addResidente(self, residente):
        newResidente = pd.DataFrame(residente.T)
        newResidente["Trilha"] = [self.__index]
        newResidente.set_index(["Trilha","Identificador"], inplace=True)
        self.__residentes = pd.concat([self.__residentes, newResidente])
    
    def getResidentes(self):
        return self.__residentes.copy()

    def setResidentes(self, residentes):
        self.__residentes = residentes
    
    def show(self):
        print("Trilha: " + self.__nome)
        print(self.__residentes)