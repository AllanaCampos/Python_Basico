import matplotlib.pyplot as plt
import pandas as pd
import obtencaoDados

class Graficos:
    def __init__(self):
        self.dow = obtencaoDados.ObterDados()
        self.cidade = None
        self.anoSelecionado = None
        self.__df = None
        self.caminhoCSV = None
    
    def dataFrame(self, cidade, anoSelecionado,anos):
        self.dow = obtencaoDados.ObterDados()
        titulos_arquivos = self.dow.downloadDados(anoSelecionado, anos)[1]
        for titulos in titulos_arquivos:
            if cidade in titulos:

                self.caminhoCSV = f'csv/{titulos}' # Atribuir valor a caminhoCSV
          
            

        self.__df = pd.read_csv(self.caminhoCSV, encoding="iso-8859-1", decimal=',', sep=';', skiprows=8)
        self.__df.index = pd.DatetimeIndex(self.__df["DATA (YYYY-MM-DD)"]+" "+self.__df["HORA (UTC)"], name="DATA") 
    
        if self.caminhoCSV is None:
            print(f"Arquivo CSV não encontrado para a cidade {cidade} no ano {anoSelecionado}")
            return  # Sair da função se o caminhoCSV não foi definido

    def tratamentoDados(self):
        self.__df.loc[self.__df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].abs() > 1000, "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"] = None
        self.__df.loc[self.__df["TEMPERATURA DO PONTO DE ORVALHO (°C)"].abs() > 1000, "TEMPERATURA DO PONTO DE ORVALHO (°C)"] = None
    
    
    def plotGraficos(self):
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
        plt.title('Precipitação Média Mensal')
        plt.xlabel('Mês')
        plt.ylabel('Precipitação')
        plt.grid(True)
        plt.subplots_adjust(wspace=0,hspace=1)
        
    def plotGrafico(cidade,anoSelecionado,anos):
        df = Graficos()
        df.dataFrame(cidade,anoSelecionado,anos)
        df.tratamentoDados()
        df.plotGraficos()
    