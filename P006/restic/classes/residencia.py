import pandas as pd
class Residencia:
    def __init__(self):
        self.__trilhas = None
    
    def attTrilhas(self, trilhas):
        self.__trilhas = pd.concat([self.__trilhas, trilhas]).drop_duplicates()
    
    def getTrilhas(self):
        return self.__trilhas.copy()
    
    def setTrilhas(self, trilhas):
        self.__trilhas = trilhas
    
    def show(self):
        print(self.__trilhas)
    