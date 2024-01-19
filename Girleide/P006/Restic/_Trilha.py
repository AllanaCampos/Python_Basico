import Restic as rt
import pandas as pd
class Trilha:
    residente = rt.Residente()
    
    def __init__(self):
        self.__dataFrameDnet = None
        self.__dataFrameJava = None
        self.__dataFramePython = None
    
    def getDataFrameDnet(self):
        return self.__dataFrameDnet.copy
    
    def getDataFrameJava(self):
        return self.__dataFrameJava.copy
    
    def getDataFramePython(self):
        return self.__dataFramePython.copy
    
    def escolhaTrilha(self):
        Opcao = int(input("Selecione a trilha na qual deseja visualizar os dados:\n1:Python\n2:Java\n.NET "))
        if Opcao == 1:
            self.dataFramePython()
        elif Opcao == 2:
            self.dataFrameJava()
        else:
            self.dataFrameDnet()

    def dataFrameDnet(self, residente):
        if residente.getTrilha() == 2:
            if self.__dataFrameDnet is None:
                self.__dataFrameDnet = residente.getDataframe().copy()
            else:
                self.__dataFrameDnet = pd.concat([self.__dataFrameDnet, residente.getDataframe()])
            print(self.__dataFrameDnet)
        
    def dataFrameJava(self, residente):
        if residente.getTrilha() == 3:
            if self.__dataFrameJava is None:
                self.__dataFrameJava = residente.getDataframe().copy()
            else:
                self.__dataFrameJava = pd.concat([self.__dataFrameJava, residente.getDataframe()])

            print(self.__dataFrameJava)
        
    def dataFramePython(self, residente):
        if residente.getTrilha() == 1:
            if self.__dataFramePython is None:
                self.__dataFramePython = residente.getDataframe().copy()
            else:
                self.__dataFramePython = pd.concat([self.__dataFramePython, residente.getDataframe()])
            print(self.__dataFramePython)