import requests
from bs4 import BeautifulSoup
import os

class ManipulacaoDeDados():
    def __init__(self):
        self._anosLinks = []

        
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
        

    



