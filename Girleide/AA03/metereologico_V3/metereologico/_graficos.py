import matplotlib.pyplot as plt
import pandas as pd
import _downloadDados

class Graficos:
    def __init__(self):
        self.dow = _downloadDados.DownloadDados()
    
    def dataFrame(self, cidade, anoSelecionado):
        tituloArquivos = self.dow.getTituloArquivos()
        for titulo in tituloArquivos:
            if titulo == cidade:
                caminhoCSV = f'csvs\{anoSelecionado}\{tituloArquivos}'
                print(caminhoCSV)
    
    def tratamentoDados(self):
        pass
    
    def plotGraficos(self):
        pass
    