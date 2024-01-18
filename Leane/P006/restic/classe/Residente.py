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
    
    def DataFrame(self):
        id = ["Identificador", "idade", "formacao", "formacaoGeral", "formacaoEspecifica", "andamentoGraduacao", "tempoFormado", "experienciaProgramacao"]
        data = [self.__identificador, self.__idade, self.__formacao,self.__formacaoGeral, self.__formacaoEspecifica, self.__andamentoGraduacao, self.__tempoFormacao, self.__experienciaProgramacao]
        df = pd.DataFrame(data, index=id)
        return df
    
    def setIdentificador(self, id):
        if(type(id)== int):
            self.__identificador = id
        else:
            raise Exception("Formado de identificador nao aceito")
        
    def setIdade(self, idade):
        ano = self.__identificador %100
        if(ano > 24):
            ano += 1900 
        else:
            ano += 2000
        #verificar se idade bate com ano
        if((date.today().year - ano) == idade or (date.today().year - ano - 1) == idade):
            self.__idade = idade
        else:
            raise Exception ("Ano de nascimento nao corresponde com idade")
        
    def setFormacao(self, formacao):
        if not isinstance(formacao, int):
            raise Exception("Formato da formação deve ser um número inteiro.")
    
        if (0 <= formacao < 4):
            self.__formacao = formacao
        else:
            raise Exception("Formação inexistente.")
        
    def setFormacaoGeral(self, formacaoGeral):
        if formacaoGeral == None:
            return
        elif self.__formacao != 0 and (0 <= formacaoGeral <= 1):
            self.__formacaoGeral = formacaoGeral
        else:
            raise Exception("Formação geral inexistente.")
        
    def setFormacaoEspecifica(self, formacaoEspecifica):
        if formacaoEspecifica == None:
            return
        elif ((0 <= self.__formacaoEspecifica <= 1) and type(self.__formacaoEspecifica) == str):
            self.__formacaoEspecifica = formacaoEspecifica
        else:
            raise Exception ("formacaoEspecifica nao válida")
        
    def setAndamentoGraduacao(self, andamentoGraduacao):
        if andamentoGraduacao == None:
            return
        elif ((1 <= self.__andamentoGraduacao <= 2) and type(andamentoGraduacao) == float):
            self.__andamentoGraduacao = andamentoGraduacao
        else: 
            raise Exception ("Tipo invalido para andamento graduacao")
        
    def setTempoFormacao(self, tempoFormacao):
        if tempoFormacao == None:
            return
        elif (type(tempoFormacao) == int and self.__formacao == 3):
            self.__tempoFormacao = tempoFormacao
        else:
            raise Exception ("Tempo de formacao nao válido")
        
    def setExperienciaProgramacao(self, experienciaProgramacao):
        if type(experienciaProgramacao) == bool:
            self.__experienciaProgramacao = experienciaProgramacao
        else:
            raise Exception ("Experiencia de programacao nao válido")
        
    
            
        
        
        
        