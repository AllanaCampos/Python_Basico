from datetime import datetime
import re
import pandas as pd
class Residente:
    
    def __init__(self):
        self.__identificador = None
        self.__dataNascimento = None
        self.__cpf = None
        self.__idade = None
        self.__formacao = None
        self.__formacaoGeral = None
        self.__formacaoEspecifica = None
        self.__andamentoGraduacao = None
        self.__tempoFormacao = None
        self.__experienciaPrevia = None

    def dadosResidente(self):
        self.__dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa):")
        self.idadeResidente()
        print(self.__idade)
        self.__cpf = input("Digite seu cpf (xxx.xxx.xxx-xx)")
        self.identificador()
        print(self.__identificador)
        print("Escolha sua formação:")
        self.__formacao = input(" 0: Formação técnica \n 1: Formação técnica \n 2: graduação em andamento \n 3: Graduação concluída")
        self.__formacaogeral = input("Qual é a sua área de formação geral? \n 0: Engenharia \n 1: Comutação")
        self.__formacaoEspecifica = input("Digite sua formação específica:")
        self.formacaoEspecifica()
        print(self.__formacaoEspecifica)
        self.__andamentoGraduacao = input("Percentual do curso: (press enter se já tiver concluido)")
        self.__tempoFormacao = input("Tempo de formado(press enter se não tiver se formado)")
        self.__experienciaProgramacao = input("Possui experiência com programação? (True/false)").lower() == 'true'
        self.dadosDataFrame()
        
    def idadeResidente(self):
        mesAtual = datetime.now().month
        anoNascimento = int(self.__dataNascimento[-4:])
        mesNascimento = int(self.__dataNascimento[3:5])
        if mesAtual > mesNascimento:
            self.__idade = datetime.now().year - anoNascimento
        elif mesAtual < mesNascimento:
            self.__idade = (datetime.now().year - anoNascimento) - 1
        else: 
            diaAtual = datetime.now().day
            diaNascimento = int(self.__dataNascimento[:2])
            if diaAtual >= diaNascimento:
                self.__idade = datetime.now().year - anoNascimento
            else:
                self.__idade = (datetime.now().year - anoNascimento) - 1
    
    def identificador(self):
        DigitosCpf = self.__cpf[:3]
        DigitosNasci = self.__dataNascimento[-2:]
        self.__identificador =  "tic18py" + DigitosCpf  + DigitosNasci
        
    def formacaoEspecifica(self):
        agrupamento = {
        'comp': 'Ciência da Computação',
        'cc': 'Ciência da Computação',
        'eng elétrica': 'Engenharia Elétrica',
        'eng elétr': 'Engenharia Elétrica',
        'eng. el.': 'Engenharia Elétrica',
        'eng el': 'Engenharia Elétrica',
        'eng quím': 'Engenharia Química',
        'eng quim': 'Engenharia Química',
        'eng. quim': 'Engenharia Química',
        'engenharia q': 'Engenharia Química',
        'eng mec': 'Engenharia Mecânica',
        'eng. mec': 'Engenharia Mecânica'    
        }
        
        for abreviacao, categoria in agrupamento.items():
            self.__formacaoEspecifica = re.sub(fr'\b{abreviacao}\b', categoria, self.__formacaoEspecifica, flags=re.IGNORECASE)

    def dadosLista(self):
        Dados = [self.__identificador, self.__idade, self.__formacao, self.__formacaoGeral,
                 self.__formacaoEspecifica, self.__andamentoGraduacao, self.__tempoFormacao,
                 self.__experienciaPrevia]
        
    def dadosDataFrame(self):
        Dados = pd.DataFrame({'Idade': self.__idade,
                      'Formacao': self.__formacao,
                      'FormacaoGeral': self.__formacaoGeral,
                      'FormacaoEspecifica': self.__formacaoEspecifica,
                      'AndamentoGraduacao': self.__andamentoGraduacao,
                      'TempoFormacao': self.__tempoFormacao,
                      'ExperienciaPrevia': self.__experienciaPrevia}, index = self.__identificador)

        Dados
            
            