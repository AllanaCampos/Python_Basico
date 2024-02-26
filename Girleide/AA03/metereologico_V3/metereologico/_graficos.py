import matplotlib.pyplot as plt
import pandas as pd
import _downloadDados

class Graficos:
    
    def __init__(self):
       self.__df = None
    
    def dataFrame(self, cidade, anoSelecionado, anos):
        self.dow = _downloadDados.DownloadDados()
        tituloArquivos = self.dow.downloadDados(anoSelecionado, anos)[1]
        for titulo in tituloArquivos:
            if cidade in titulo:
                caminhoCSV = f'csvs/{titulo}'
                
        self.__df = pd.read_csv(caminhoCSV,encoding="iso-8859-1", decimal=',', sep=';', skiprows=8)


    def tratamentoDados(self):

        self.__df.rename({"DATA (YYYY-MM-DD)":"Data","HORA (UTC)":"Hora","Hora UTC":"Hora"},axis=1,inplace=True)
        self.__df.index = pd.DatetimeIndex(self.__df["Data"]+" "+self.__df["Hora"], name="DATA")
        self.__df.loc[self.__df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].abs() > 1000, "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"] = None
        self.__df.loc[self.__df["TEMPERATURA DO PONTO DE ORVALHO (°C)"].abs() > 1000, "TEMPERATURA DO PONTO DE ORVALHO (°C)"] = None
    
    def plotGrafTemp(self):
        
        df = self.__df.groupby(self.__df.index.month)["TEMPERATURA DO PONTO DE ORVALHO (°C)"].mean()
        plt.clf()
        plt.subplot(2,1,1)
        plt.plot(df.index, df, marker='s')
        plt.title('Temperatura Média Mensal')
        plt.xlabel('Mês')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)

        dfT = self.__df.groupby(self.__df.index.month)["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].sum()
        plt.subplot(2,1,2)
        plt.plot(dfT.index, dfT, marker='s')
        plt.title('Precipitação Acumulada Mensal')
        plt.xlabel('Mês')
        plt.ylabel('Precipitação')
        plt.grid(True)
        plt.subplots_adjust(wspace=0,hspace=1)
    
    def plotGrafico(cidade,anoSelecionado,anos):
        df = Graficos()
        df.dataFrame(cidade,anoSelecionado,anos)
        df.tratamentoDados()
        df.plotGrafTemp()
        

        
    