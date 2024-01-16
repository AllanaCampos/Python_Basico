from ..classes import Residente, Trilha, Residencia
import pandas as pd
import os.path

def menu():
    op = 1
    trilhaPython = Trilha("Python", "tic18Py")
    trilhaNet = Trilha("Net", "tic18Net")
    trilhaJava = Trilha("Java", "tic18Jav")
    tic18 = Residencia()
    df = None
    if(os.path.isfile("tic18.csv")): 
        df = pd.read_csv("tic18.csv", index_col=['Trilha','Identificador'])
        tic18.setTrilhas(df)

    while(op != 0):
        print("<----------MENU---------->")
        print("1- Cadastrar residente")
        print("2- Atualizar residência")
        print("3- Mostrar trilhas")
        print("0- Sair")

        op = int(input())
        try:
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
                case 2:
                    tic18.attTrilhas(pd.concat([trilhaJava.getResidentes(), trilhaPython.getResidentes(), trilhaNet.getResidentes()]))
                case 3:
                    tic18.mostrarTrilhas()
        except Exception as e:
            print(e)
            

def cadastrarResidente():
    residente = Residente()
    print("Informe os três primeiros dígitos do CPF")
    cpf = int(input())
    print("Informe os dois ultimos dígitos do ano de nascimento")
    ano = int(input())
    print("Informe a idade")
    idade = int(input())
    print("Informe o perfil de formação (0-3)")
    print("0- Formação técnica\n1- Formação técnica graduação em andamento\n2- Graduação em andamento\n3- Graduação concluída")
    formacao = int(input())
    formacaoGeral = None
    formacaoEspecifica = None
    andamentoGraduacao = None
    tempoFormacao = None
    if(formacao != 0):
        print("Informe a área de formação geral(0-1)")
        print("0- Engenharia\n1- Computação")
        formacaoGeral = int(input())
    if(formacaoGeral == 0 or formacaoGeral == 1):
        print("Informe o nome do curso")
        formacaoEspecifica = input()
    if(formacao == 1 or formacao == 2):
        print("Informe o percentual de curso concluído")
        andamentoGraduacao = float(input())
    if(formacao == 3):
        print("Informe a quantidades de anos de formado")
        tempoFormacao = int(input())
    print("Tinha experiência prévia em programação?\n1- Sim\n2- Não")
    experienciaProgramacao = int(input())
    if(experienciaProgramacao == 1): experienciaProgramacao = True
    if(experienciaProgramacao == 2): experienciaProgramacao = False
    print("Informe a trilha a qual o residente participa")
    print("1- Python\n2- .NET\n3- Java")
    trilha = int(input())
    try:
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
        print(e)
    

