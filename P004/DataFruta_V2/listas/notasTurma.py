import numpy as np
class NotasTurma:
    def __init__(self, nAlunos = 30, nCreditos = 3):
        self.notas = np.zeros((nAlunos, nCreditos))
    
    def leNotas(self):
        for i in range(len(self.notas)):
            for j in range(len(self.notas[0])):
                print("Informe a nota do crédito " + str(j+1) + " do aluno " + str(i+1))
                nota = float(input())
                self.notas[i,j] = nota
    
    def mediaTurma(self):
        return self.notas.mean()
    
    def mediaAluno(self, index = 0):
        return self.notas[index].mean()
    
    def mediaAvaliacao(self, index = 0):
        return self.notas[:, index].mean()
    
    def quantAprovados(self):
        aprovados = self.notas.mean(axis=1) >= 6
        return aprovados.sum()
    
    def quantReprovados(self):
        reprovados = self.notas.mean(axis=1) < 6
        return reprovados.sum()
    
    def menorNota(self):
        menorNotaAvaliacao = self.notas.min(axis=0)
        menorMedia = self.notas.mean(axis=1).min()
        return menorNotaAvaliacao, menorMedia
    
    def maiorNota(self):
        maiorNotaAvaliacao = self.notas.max(axis=0)
        maiorMedia = self.notas.mean(axis=1).max()
        return maiorNotaAvaliacao, maiorMedia
    
    def __str__(self):
        txt = "Alunos\t|\tNotas\n"
        for i in range(len(self.notas)):
            txt += (str(i) + "\t|\t" + str(self.notas[i]) + "\n")
        return txt
    
        

        







