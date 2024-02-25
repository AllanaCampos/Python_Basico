import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import re

class BuscaDados:
    
    def __init__(self, anos, erro):
        self.__anos = anos
        self.__erro = erro
    
    def buscaDados(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        url = "https://portal.inmet.gov.br/dadoshistoricos"
        self.__anos = []
        self.__erro= None
        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()
        except HTTPError as http_err:
            self.__erro = http_err
        except Exception as err:
            self.__erro = err
        else:
            respostaHtml = BeautifulSoup(resposta.text, 'html.parser')
            anosTag = respostaHtml.find_all('article')
            for ano in anosTag:
                anoFormat = re.search(r'\d{4}', ano.find('a').string)
                self.__anos.append((anoFormat.group(), ano.find('a')['href']))

        return self.__anos, self.__erro