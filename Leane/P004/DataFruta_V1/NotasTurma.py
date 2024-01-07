import numpy as np

class NotasTurma:
   
    def __init__(self, nAlunos = 30, nCreditos = 3):
        self.notas = np.zeros ((nAlunos, nCreditos))
        
    def leNotas(self):
        for i in range(self.notas.shape[0]):    #linha alunos
            for j in range(self.notas.shape[1]):   #colunas notas 
                nota = float(input(f"Informe a nota do crédito {j+1} do aluno {i+1}: "))
                self.notas[i, j] = nota
                
    def mediaTurma(self):
        mediaTurma = self.notas.mean()
        return mediaTurma
    
    def mediaAluno(self, index = 0):
        mediaAluno = self.notas[index].mean()
        return mediaAluno
    
    def mediaAvaliaçao(self, index = 0):
        mediaTurmaAvali = self.notas[:, index].mean()
        return mediaTurmaAvali
    
    def quantAprovados(self):
        alunosAprov = self.notas.mean(axis=1) >=6 
        aprovados = alunosAprov.sum()
        return aprovados
    
    def quantReprovados(self):
        alunosRepro = self.notas.mean(axis=1) < 6
        reprovados = alunosRepro.sum()
        return reprovados
    
    def menorNota(self):
        menorMediaAvaliacoes = self.notas.mean(axis=1).min()
        menorNotaAvali = self.notas.min(axis=0)
        return menorMediaAvaliacoes, menorNotaAvali
        
    def maiorNota(self):
        maiorMediaAvaliacoes = self.notas.mean(axis=1).max()
        menorNotaAvali = self.notas.max(axis=0)
        return maiorMediaAvaliacoes, menorNotaAvali
    
    def __str__(self):
        pass