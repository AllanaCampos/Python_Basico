from restic.classe import Trilha, Residencia, Residente

import pandas as pd
import os.path

def menu():
    op = 1
    trilhaPython = Trilha("Python", "tic18Py")
    trilhaNet = Trilha("Net", "tic18Net")
    trilhaJava = Trilha("Java", "tic18Jav")
    tic18 = Residencia()
    
    getDataFrame(tic18, trilhaPython, trilhaJava, trilhaNet)

    while(op != 0):
        print("<----------MENU---------->")
        print("1- Cadastrar residente")
        print("2- Mostrar trilhas")
        print("3- Mostrar residência")
        print("0- Sair")

        op = int(input())
        match op:
            case 0:
                tic18.getTrilhas().to_csv('tic18.csv')
            case 1: 
                residente, trilha = cadastrarResidente()
                if(trilha == 1):
                    trilhaPython.addResidente(residente.makeDataFrame())
                elif(trilha == 2):
                    trilhaNet.addResidente(residente.makeDataFrame())
                elif(trilha == 3):
                    trilhaJava.addResidente(residente.makeDataFrame())
                tic18.attTrilhas(pd.concat([trilhaJava.getResidentes(), trilhaPython.getResidentes(), trilhaNet.getResidentes()]))
            case 2:
                mostrarTrilhas(trilhaPython, trilhaJava, trilhaNet)
            case 3:
                tic18.show()

def getDataFrame(residencia, trilhaPython, trilhaJava, trilhaNet):
    if(os.path.isfile("tic18.csv")): 
        df = pd.read_csv("tic18.csv", index_col=['Trilha','Identificador'])
        residencia.setTrilhas(df)
        if("tic18Py" in [trilha[0] for trilha in df.index.values]):
            trilhaPython.setResidentes(df.loc[(['tic18Py'],), :] )
        if("tic18Jav" in [trilha[0] for trilha in df.index.values]):
            trilhaJava.setResidentes(df.loc[(['tic18Jav'],), :] )
        if("tic18Net" in [trilha[0] for trilha in df.index.values]):
            trilhaNet.setResidentes(df.loc[(['tic18Net'],), :] )
           
def mostrarTrilhas(trilhaPython, trilhaJava, trilhaNet):
    print("Informe a trilha que deseja observar")
    print("1- Python")
    print("2- Java")
    print("3- .NET")
    try:
        trilha = int(input())
        match trilha:
            case 1:
                trilhaPython.show()
            case 2:
                trilhaJava.show()
            case 3:
                trilhaNet.show()
    except Exception as e:
        print(e)


def cadastrarResidente():
    try:
        formacaoGeral = None
        formacaoEspecifica = None
        andamentoGraduacao = None
        tempoFormacao = None
        trilha = None
        residente = Residente()
        cpf = int(input("Informe os três primeiros dígitos do CPF: "))
        ano = int(input("Informe os dois ultimos dígitos do ano de nascimento: "))
        idade = int(input("Informe a idade: "))
        texto = "Informe o perfil de formação (0-3)\n0- Formação técnica\n1- Formação técnica graduação em andamento\n2- Graduação em andamento\n3- Graduação concluída\n"
        formacao = -1
        while(formacao != 0 or formacao != 1 or formacao != 2 or formacao != 3):
            formacao = int(input(texto))
        if(formacao != 0):
            while (formacaoGeral != 0 and formacaoGeral != 1):
                formacaoGeral = int(input("Informe a área de formação geral(0-1)\n0- Engenharia\n1- Computação\n"))
        if(formacaoGeral == 0 or formacaoGeral == 1):
            formacaoEspecifica = input("Informe o nome do curso: ")
        if(formacao == 1 or formacao == 2):
            andamentoGraduacao = float(input("Informe o percentual de curso concluído: "))
        if(formacao == 3):
            tempoFormacao = int(input("Informe a quantidades de anos de formado:"))
        while(experienciaProgramacao != 1 and experienciaProgramacao != 2):
            experienciaProgramacao = int(input("Tinha experiência prévia em programação?\n1- Sim\n2- Não\n"))
            if(experienciaProgramacao == 1): experienciaProgramacao = True
            elif(experienciaProgramacao == 2): experienciaProgramacao = False
        while(trilha != 1 and trilha != 2 and trilha != 3):
            trilha = int(input("Informe a trilha a qual o residente participa\n1- Python\n2- .NET\n3- Java"))
        
        residente.setIdentificador(cpf*100 + ano)
        residente.setIdade(idade)
        residente.setFormacao(formacao)
        residente.setFormacaoGeral(formacaoGeral)
        residente.setFormacaoEspecifica(formacaoEspecifica)
        residente.setAndamentoGraduacao(andamentoGraduacao)
        residente.setTempoFormacao(tempoFormacao)
        residente.setExperienciaProgramacao(experienciaProgramacao)
        return residente, trilha
    except Exception as e:
        print(e + "\nTente novamente")
    
