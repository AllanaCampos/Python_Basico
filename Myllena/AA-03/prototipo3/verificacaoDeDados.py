import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt

class VerificacaoDeDados():
    
    # CLASSE PARA ABRIR O ARQUIVO CSV, TRANSFORMAR EM UM DATA FRAME DO PANDAS, FILTRAR DADOS E PLOTAR P GRÁFICO 
    def __init__(self,csv):
        
    # CONSTRUTOR DA CLASSE QUE RECEBE O CAINHO DO CSV COMO PARAMETRO
    # RENOMEIA O TITULO DO DATA FRAME
       
        self._df = pd.read_csv(csv, encoding='iso-8859-1', decimal=',', delimiter=';', skiprows=8)
        self._df.rename({"DATA (YYYY-MM-DD)":"Data","HORA (UTC)":"Hora","Hora UTC":"Hora"},axis=1,inplace=True)
        self._df.index = pd.DatetimeIndex(self._df["Data"]+" "+self._df["Hora"], name="DATA")


    def filtraDados(self):
        # FUNÇÃO QUE FILTRA OS DADOS PRENCHIDOS DE MODO A REPRESENTAR OS DADOS FALTANTE
        
        self._df.loc[self._df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].abs() > 1000, "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"] = nan
        self._df.loc[self._df["TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"].abs() > 1000, "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"] = nan
    

    def geraGraficos(self):
        
        # CALCULANDO A MÉDIA MENSAL DA TEMPERATURA DO AR E DA PRECIPITAÇÃO PLOTANDO O GRAFICO AO LONGO DOS MESES
        plt.clf()
        plt.subplot(2,1,1)
        self._df.groupby(self._df.index.month)["TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"].mean().plot(
            ylabel="TEMPERATURA (°C)",
            xlabel="MÊS",
            title="TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",
            marker="s", 
            color = "Red")
        plt.grid()
        
        plt.subplot(2,1,2)
        self._df.groupby(self._df.index.month)["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].sum().plot(
            ylabel="PRECIPITAÇÃO (mm)",
            xlabel="MÊS",
            title="PRECIPITAÇÃO MÉDIA MENSAL ",
            marker="s",
            color = "Red")
        plt.grid()
        plt.subplots_adjust(wspace=1,hspace=1)

        return plt.gcf()
    
    def plotGrafico(csv):
        grafico = VerificacaoDeDados(csv)
        grafico.filtraDados()
        return grafico.geraGraficos()