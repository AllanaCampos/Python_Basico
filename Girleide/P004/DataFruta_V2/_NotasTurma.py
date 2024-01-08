class NotasTurma:
    
    def __init__(self, nAlunos = 30, nCreditos = 3):
        super().__init__()
        self._nAlunos = nAlunos
        self._nCreditos = nCreditos
        self._notas = [[0] * nCreditos for _ in range(nAlunos)]

    def leNotas(self):
        for i in range(self._nAlunos):
            for j in range(self._nCreditos):
                nota = float(input(f"Informe a nota do aluno {i + 1} na disciplina {j + 1}: "))
                self._notas[i][j]=nota

    def mediaTurma(self):
        notas = [nota for sublist in self._notas for nota in sublist]
        return sum(notas) / len(notas) if notas else 0

    def mediaAluno(self, index = 0):
        if 0 <= index < self._nAlunos:
            notas_aluno = self._notas[index]
            return sum(notas_aluno) / len(notas_aluno) if notas_aluno else 0
        else:
            print("Índice de aluno inválido.")
            return 0
        
    def mediaAvaliaçao(self, index = 0):
        if 0 <= index < self._nCreditos:
            notasAvaliacao = [notas[index] for notas in self._notas]
            return sum(notasAvaliacao) / len(notasAvaliacao) if notasAvaliacao else 0
        else:
            print("Índice de avaliação inválido.")
            return 0

    def quantAprovados(self):
        aprovados = sum(1 for notasAluno in self._notas if self.mediaAluno(self._notas.index(notasAluno)) >= 6)
        return aprovados

    def quantReprovados(self):
        reprovados = sum(1 for notasAluno in self._notas if self.mediaAluno(self._notas.index(notasAluno)) < 6)
        return reprovados
 
    def menorNota(self):
        notasAvaliacoes = [min(notas) for notas in zip(*self._notas)]
        menorMediaFinal = min(self.calcular_media(), min(notasAvaliacoes))
        return notasAvaliacoes + [menorMediaFinal]

    def maiorNota(self):
        notasAvaliacoes = [max(notas) for notas in zip(*self._notas)]
        maiorMediaFinal = max(self.calcular_media(), max(notasAvaliacoes))
        return notasAvaliacoes + [maiorMediaFinal]

    def __str__(self):
        return str(self._notas) 
    
    def calcular_media(self):
        import numpy as np
        return np.mean(self._notas)