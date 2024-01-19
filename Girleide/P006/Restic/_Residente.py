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
        self.__trilha = None
        self.__dados = None
        self.__Dataframe = None
        
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
        
    def dataNascimento(self):
        
        while True:
            self.__dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa):")
            if re.match(r'^\d{2}/\d{2}/\d{4}$', self.__dataNascimento):
                break
            else:
                print("Formato de data inválido. Digite novamente.")
       
    def cpf(self):
          while True:
            self.__cpf = input("Digite seu cpf (Apenas números)")
            if len(self.__cpf) == 11 and self.__cpf.isdigit():
                break
            else:
                print("CPF inválido. Digite novamente.")
       
    def identificador(self):
        DigitosCpf = self.__cpf[:3]
        DigitosNasci = self.__dataNascimento[-2:]
        if (self.__trilha == 1):
            self.__identificador =  "tic18py" + DigitosCpf  + DigitosNasci
        elif (self.__trilha == 2):
            self.__identificador =  "tic18dn" + DigitosCpf  + DigitosNasci
        elif (self.__trilha == 3):
            self.__identificador =  "tic18ja" + DigitosCpf  + DigitosNasci
        else:
            print("Opção inválida")   
                     
    def formação(self): 
        
        while True:
            print("------Escolha sua formação------")
            self.__formacao = int(input(" 0: Formação técnica \n 1: Formação técnica graduação em andamento \n 2: graduação em andamento \n 3: Graduação concluída \n"))
            if (self.__formacao != 0 and self.__formacao != 1 and self.__formacao != 2 and self.__formacao != 3):
                print("Escolha uma opção válida")
            else:
                break
            
    def formacaoGeral(self):
        while True:
            self.__formacaoGeral = int(input("Qual é a sua área de formação geral? \n 0: Engenharia \n 1: Computação \n"))
            if (self.__formacaoGeral != 0 and self.__formacaoGeral != 1):
                print("Escolha uma opção válida")
            else:
                break

    def formacaoEspecifica(self):
        self.__formacaoEspecifica = input("Digite sua formação específica:")
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
                
    def andamentoGraduação(self):
        while True:
            entrada = input("Percentual do curso: (pressione Enter se já tiver concluído): ")
            if entrada.strip() == '':
                self.__andamentoGraduacao = None
                break
            elif entrada.replace('.', '', 1).isdigit():
                self.__andamentoGraduacao = float(entrada)
                break
            else:
                print("Entrada inválida. Digite um número ou pressione Enter.")
        
    def tempoFormacao(self):
        if  (self.__andamentoGraduacao == None):
            self.__tempoFormacao = input("Tempo de formado(press enter se não tiver se formado)")
        else:
            self.__tempoFormacao = None 
            
    def experiênciaProgramacao(self):
       while True:
            resposta = input("Possui experiência com programação? (True/False): ").lower()
            if resposta in ['true', 'false']:
                self.__experienciaPrevia = resposta == 'true'
                break
            else:
                print("Resposta inválida. Digite 'True' se possui experiência ou 'False' se não possui.")
                
    def dadosResidente(self):
        self.__trilha = int(input("A qual trilha pertence? \n 1-python \n 2-.NET \n 3 -java"))
        self.dataNascimento()
        self.idadeResidente()
        self.cpf()
        self.identificador()
        self.formação()
        self.formacaoGeral()
        self.formacaoEspecifica()
        self.andamentoGraduação()
        self.tempoFormacao()
        self.experiênciaProgramacao()
        self.dadosDataFrame()
        print(self.__Dataframe)

   
    def dadosDataFrame(self):
         
        self.__dados = {
            'identificador': [self.__identificador],
            'Idade': [self.__idade],
            'Formacao': [self.__formacao],
            'FormacaoGeral': [self.__formacaoGeral],
            'FormacaoEspecifica': [self.__formacaoEspecifica],
            'AndamentoGraduacao': [self.__andamentoGraduacao],
            'TempoFormacao': [self.__tempoFormacao],
            'ExperienciaPrevia': [self.__experienciaPrevia]  
        }
        self.__Dataframe = pd.DataFrame(self.__dados)
        self.__Dataframe.set_index('identificador', inplace=True)