from bs4 import BeautifulSoup
import requests
import wget
import zipfile
def getAnos():
    url = 'https://portal.inmet.gov.br/dadoshistoricos'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    requisicao = requests.get(url, headers=headers)

    texto = BeautifulSoup(requisicao.text, 'html.parser')
    a = texto.find_all('article')
    ano =  []
    link = []
    for i in a:
        ano.append(i.find('a').string)
        link.append(i.find('a')['href'])
        print(i)

    #print(i.find('a')['href'])
    #wget.download(link[-1], ano[-1]+'.zip')

    

#with zipfile.ZipFile('arquivo.zip', 'r') as zip:
#    zip.extractall()
    
getAnos()
