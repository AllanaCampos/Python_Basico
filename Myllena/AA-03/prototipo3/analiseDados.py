import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt

class AnaliseDados():
    """
        Classe responsavel por abrir o arquivo csv, transforma-lo em um Pandas.DataFrame, filtrar os dados e gerar os graficos
    """
    def __init__(self,csv):
        """
            Construtor da classe recebe o caminho para o arquivo csv como parametro
        """
        self._df = pd.read_csv(csv, encoding='iso-8859-1', decimal=',', delimiter=';', skiprows=8)
        self._df.rename({"DATA (YYYY-MM-DD)":"Data","HORA (UTC)":"Hora","Hora UTC":"Hora"},axis=1,inplace=True)
        self._df.index = pd.DatetimeIndex(self._df["Data"]+" "+self._df["Hora"], name="DATA")


    def filtraDados(self):
        """
            Metodo resposavel por filtrar dados preenchidos de modo a represebtar dados faltando
        """
        self._df.loc[self._df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].abs() > 1000, "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"] = nan
        self._df.loc[self._df["TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"].abs() > 1000, "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"] = nan
    

    def geraGraficos(self):
        """
            Metodo responsavel por gerar os graficos de temperatura media mensal do ponto de orvalho e de precipitação media mensal 
        """
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
        self._df.groupby(self._df.index.month)["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].mean().plot(
            ylabel="PRECIPITAÇÃO (mm)",
            xlabel="MÊS",
            title="PRECIPITAÇÃO MÉDIA MENSAL ",
            marker="o",
            color = "Red")
        plt.grid()
        plt.subplots_adjust(wspace=1,hspace=1)

        return plt.gcf()
    
    def plotGrafico(csv):
        grafico = AnaliseDados(csv)
        grafico.filtraDados()
        return grafico.geraGraficos()


        