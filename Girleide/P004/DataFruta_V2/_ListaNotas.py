from .analiseDados import AnaliseDados
import random

class NotasTurma(AnaliseDados):
    
    def __init__(self, nAlunos = 30, nCreditos = 3):
        super().__init__()
        self._nAlunos = nAlunos
        self._nCreditos = nCreditos
        self._notas = [[0] * nCreditos for _ in range(nAlunos)]
    
    def addNota(self):
        print("Informe a nota")
        nota = float(input())
        self._notas.append(nota)     

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de notas")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a nota {i+1}:")
            valor = float(input())
            self._notas.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self._notas)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = NotasTurma.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado    

    def mostraMenor(self):
        listaOrdenada = sorted(self._notas)
        return listaOrdenada[0]

    def mostraMaior(self):
        listaOrdenada = sorted(self._notas)
        return listaOrdenada[listaOrdenada.__len__() - 1]
    
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media
    
    def geraListaNotas(n, nMin = 0, nMax = 10):
        listaNotasAleatorias = [random.uniform(nMin, nMax) for _ in range(n)]
        return NotasTurma(listaNotasAleatorias)

    def calculaMediaAritmetica(self):
        mediaAritmetica = sum(self._notas)/len(self._notas)
        return mediaAritmetica
        
    def medianaSuperior(self):
        dadosOrdenados = sorted(self._notas)
        n = len(dadosOrdenados)
        indiceMedianaSuperior = (n + 1) // 2
        medianaSuperior = dadosOrdenados[indiceMedianaSuperior]
        return medianaSuperior
    
    def medianaInferior(self):
        dadosOrdenados = sorted(self._notas)
        n = len(dadosOrdenados)
        indiceMedianaInferior = n // 2
        medianaInferior = dadosOrdenados[indiceMedianaInferior - 1]
        return medianaInferior
    
    def mediaGeometrica(self):
        produto = 1.0
        n = len(self._notas)
        for numero in self._notas:
            produto *= numero
        mediaGeometrica = produto ** (1 / n)
        return mediaGeometrica

    def mediaHarmonica(self):
        soma = 0
        for numero in self._notas:
            if numero == 0:
                raise ValueError("erro")
            soma += 1 / numero
        mediaHarmonica = len(self._notas) / soma
        return mediaHarmonica

    def desvioPadraoPopulacional(self):
        somaQuadrados = sum((x - self.calculaMediaAritmetica()) ** 2 for x in self._notas)
        desvio = (somaQuadrados/len(self._notas)) ** (1/2)
        return desvio
    
    def varianciaPopulacional(self):
       varianciaPopulacio =  self.desvioPadraoPopulacional() ** 2
       return varianciaPopulacio
   
    def desvioPadraoAmostral(self):
        somaQuadrados = sum((x - self.calculaMediaAritmetica()) ** 2 for x in self._notas)
        desvio = (somaQuadrados/(len(self._notas) -1)) ** (1/2)
        return desvio
    
    def varianciaAmostral(self):
        varianciaAmostra =  self.desvioPadraoAmostral() ** 2
        return varianciaAmostra
    
    def moda(self):
        frequencias = {}
        for nota in self._notas:
            if nota in frequencias:
                frequencias[nota] += 1
            else:
                frequencias[nota] = 1
        modaValor = max (frequencias, key = frequencias.get)
        modaContagem = frequencias[modaValor]
        modas = [valor for valor, contagem in frequencias.items() if contagem == modaContagem]
        return modas

    def leNotas(self):
        for i in range(self._nAlunos):
            for j in range(self._nCreditos):
                nota = float(input(f"Informe a nota do aluno {i + 1} na disciplina {j + 1}: "))
                self.addNota(i, j, nota)

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