import requests
from bs4 import BeautifulSoup

class BuscaDados:
    
    def __init__(self, anos, erros):
        self.__anos = anos
        self.__erros = erros
    
    def obter_anos_disponiveis(self):
        
        self.__anos =  []
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        url = "https://portal.inmet.gov.br/dadoshistoricos"
        
        resposta = requests.get(url, headers=headers)
        
        self.__erros= None
        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()
        except requests.HTTPError as http_err:
            self.__erros = http_err
        except Exception as err:
            self.__erros = err
        else:
            texto = BeautifulSoup(resposta.text, 'html.parser')
            articles = texto.find_all('article')
            for i in articles:
                ano_string = i.find('a').string
                ano_formatado = ''.join(filter(str.isdigit, ano_string))
                self.__anos.append((ano_formatado, i.find('a')['href']))
        
        return self.__anos, self.__erros
 