import requests
from bs4 import BeautifulSoup
import wget
import zipfile
import os

class ManipulacaoDeDados():
    def __init__(self):
        self._anosLinks = []
        self._path="./climaplotDonwloads/"

        if not os.path.exists(self._path):
            os.makedirs(self._path)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            resposta = requests.get("https://portal.inmet.gov.br/dadoshistoricos", headers=headers)

        

            html = BeautifulSoup(resposta.text, 'html.parser')
        
            articlesTag = html.find_all('article')


            for article in articlesTag:
                link = article.find('a')["href"]
                
                ano = article.find('a').string.split(" ")[1]
                self._anosLinks.append({"ano":ano,"link":link})
        except:
            pass

    

    def getDados(self):
        return self._anosLinks

    def getPath(self):
        return self._path
        

    def donwloadCSV(dado,path):

        ano = dado["ano"]
        link = dado["link"]

        pathArquivo = os.path.join(path, ano + ".zip")

        
        if  not ano+".zip" in os.listdir(path):
            wget.download(link,pathArquivo)
            with zipfile.ZipFile(pathArquivo,"r") as zip:
                if  zip.namelist()[0].split("/")[0] == ano:
                    zip.extractall(path)
                else:
                    zip.extractall(path+"/"+ano+"/")
    

    def getEstacoes(ano,path):
        estacoes = []
        try:
            files = os.listdir(path+ano+"/")
            for file in files:
                estacoes.append({
                    "estação":file.split("_")[4],
                    "path": os.path.join(path,ano, file)})
        except Exception:
            print(f"Não há dados de estações baixadas para o ano {ano}")

        return estacoes
    



