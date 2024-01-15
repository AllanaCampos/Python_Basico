import pandas as pd
class Residencia:
    def __init__(self):
        self.__trilhas = None
    
    def attTrilhas(self, trilhas):
        self.__trilhas = pd.concat(trilhas)
        print(self.__trilhas)
    