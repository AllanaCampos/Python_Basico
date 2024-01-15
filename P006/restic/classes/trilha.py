import pandas as pd
class Trilha:
    def __init__(self, nome, id):
        self.__index = id
        self.__residentes = pd.DataFrame([])
        self.__nome = nome
    
    def addResidente(self, residente):
        newResidente = pd.DataFrame(residente.T)
        newResidente.index = [self.__index]
        self.__residentes = pd.concat([self.__residentes, newResidente])
    
    def getResidentes(self):
        return self.__residentes.copy()