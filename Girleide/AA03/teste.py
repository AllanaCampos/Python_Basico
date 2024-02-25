import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import re
import wget

def buscaDados():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = "https://portal.inmet.gov.br/dadoshistoricos"
    anos = []
    erro = None
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
    except HTTPError as http_err:
        erro = http_err
    except Exception as err:
        erro = err
    else:
        respostaHtml = BeautifulSoup(resposta.text, 'html.parser')
        anosTag = respostaHtml.find_all('article')
        for ano in anosTag:
            anoFormat = re.search(r'\d{4}', ano.find('a').string)
            anos.append((anoFormat.group(), ano.find('a')['href']))

    return anos, erro

def downloadDados(anoSelecionado, anos):
    link = None
    for ano in anos:
        if ano[0] == anoSelecionado:
            link = ano[1]
            wget.download(link, f'csvs/{anoSelecionado}.zip')

    if link is None:
        print(f"Não foi possível encontrar o link para o ano {anoSelecionado}")

def interface():
    app = tk.Tk()
    app.title("Dados Meteorológicos")
    app.geometry('500x300')
    app.configure(background='#c38680')
    anos, erro = buscaDados()

    if erro:
        mensagemErro = tk.Label(app, text=f"Erro ao obter dados: {erro}", background='#c38680', wraplength=450)
        mensagemErro.place(x=10, y=70, width=450, height=30)
    else:
        opcao = tk.StringVar(app)
        opcao.set(anos[0][0])
        texto1 = tk.OptionMenu(app, opcao, *[ano[0] for ano in anos],
                               command=lambda anoSelecionado: downloadDados(anoSelecionado, anos))
        texto1.place(x=10, y=10, width=100, height=50)
        
    app.mainloop()

def main():
    interface()

if __name__ == '__main__':
    main()
