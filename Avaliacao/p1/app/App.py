import tkinter as tk
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import requests

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Dados Meteorológicos')
        self.geometry('720x500')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.tree = self.create_tree_widget()
        

    def create_tree_widget(self):
        tree = ttk.Treeview(self, selectmode='browse')
        tree.heading('#0', text='Anos', anchor=tk.W)

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky=tk.NSEW)

        ano, link = self.getDados()
        id = 0
        for i in ano:
            tree.insert('', tk.END, text=i.split(' ')[1], iid=id, open=False, values=link[id])
            id+=1

        return tree

    
    def getDados(self):
        url = 'https://portal.inmet.gov.br/dadoshistoricos'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        requisicao = requests.get(url, headers=headers)
        if requisicao.status_code != 200:
            messagebox.showerror(title="Erro de aquisição de dados", message="Não foi possível obter os dados tente novamente")
            self.destroy()
        texto = BeautifulSoup(requisicao.text, 'html.parser')
        articles = texto.find_all('article')
        ano =  []
        link = []
        for i in articles:
            ano.append(i.find('a').string)
            link.append(i.find('a')['href'])
        return ano, link