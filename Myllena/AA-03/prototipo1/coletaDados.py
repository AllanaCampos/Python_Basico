import requests
from bs4 import BeautifulSoup


class ColetaDados():
    def __init__(self):
        self._anosLinks = []

        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        # CRIANDO A REQUISIÇÃO PARA ACESSAR OS DADOS
        try:
            resposta = requests.get("https://portal.inmet.gov.br/dadoshistoricos", headers=headers)

        
        # COLETANDO INFORMAÇÕES DO SITE PEGANDO HTML DO SITE EM FORMA DE TEXTO
            html = BeautifulSoup(resposta.text, 'html.parser')
        
        # MOSTRANDO A PRIMEIRA TAG DO HTML ARTICLE CHAMADA ARTICLE
            articlesTag = html.find_all('article')

        # PEGANDO TODOS OS ARTICLE DA PAGINA QUE CONTEM 
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