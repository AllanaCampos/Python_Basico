from datetime import date
import pandas as pd
class Residente:
    def __init__(self):
        self.__identificador = None
        self.__idade = None
        self.__formacao = None
        self.__formacaoGeral = None
        self.__formacaoEspecifica = None
        self.__andamentoGraduacao = None
        self.__tempoFormacao = None
        self.__experienciaProgramacao = None
    
    def setIdentificador(self, id):
        if(type(id) ==  int):
            self.__identificador = id
        else:
            raise Exception("Formato do identificador não é semelhante ao desejado.")
    
    def setIdade(self, idade):
        ano = self.__identificador % 100
        if(ano > 24):
            ano += 1900 
        else:
            ano += 2000
        if((date.today().year - ano) == idade or (date.today().year - ano - 1)  == idade):
            self.__idade = idade
        else:
            raise Exception("Idade não corresponde ao ano de nascimento.")
    
    def setFormacao(self, formacao):
        if(0 <= formacao < 4 ):
            self.__formacao = formacao
        else:
            raise Exception("Formação inexistente.")
        
    def setFormacaoGeral(self, formacaoGeral):
        if(formacaoGeral == None): return
        elif(self.__formacao != 0 and (0 <= formacaoGeral <= 1)):
            self.__formacaoGeral = formacaoGeral
        else:
            raise Exception("Formação geral inexistente.")
    
    def setFormacaoEspecifica(self, formacaoEspecifica):
        if(formacaoEspecifica == None): return
        elif(( 0 <= self.__formacaoGeral <= 1) and type(formacaoEspecifica) == str):
            self.__formacaoEspecifica = formacaoEspecifica
        else:
            raise Exception("Formação específica inadequada.")
    
    def setAndamentoGraduacao(self, andamentoGraduacao):
        if(andamentoGraduacao == None): return
        elif( (1 <= self.__formacao <= 2) and type(andamentoGraduacao) == float):
            self.__andamentoGraduacao = andamentoGraduacao
        else:
            raise Exception("Formato incorreto.")
        
    def setTempoFormacao(self, tempoFormacao):
        print(tempoFormacao, self.__formacao)
        if(tempoFormacao == None): return
        elif (type(tempoFormacao) == int and self.__formacao == 3):
            self.__tempoFormacao = tempoFormacao
        else:
            raise Exception("Tempo de formação não corresponde com o andamento da graduação ou formato incorreto.")
    
    def setExperienciaProgramacao(self, experienciaProgramacao):
        if(type(experienciaProgramacao) == bool):
            self.__experienciaProgramacao = experienciaProgramacao
        else:
            raise Exception("Formato incorreto.")
    
    def makeDataFrame(self):
        id = ["Identificador", "Idade", "Formação", "Formação Geral", "Formação Específica", "Porcentagem Graduação", "Tempo de Formado", "Experiencia em Programação"]
        data = [self.__identificador, self.__idade, self.__formacao, self.__formacaoGeral, self.__formacaoEspecifica, self.__andamentoGraduacao, self.__tempoFormacao, self.__experienciaProgramacao]
        return pd.DataFrame(data, index=id)