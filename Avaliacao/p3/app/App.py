import tkinter as tk
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import os
import shutil
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import wget
import zipfile
import pandas as pd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Dados Meteorológicos')
        self.geometry('720x500')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.tree = self.create_tree_widget()
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        

    def create_tree_widget(self):
        tree = ttk.Treeview(self, selectmode='browse')
        tree.heading('#0', text='Anos', anchor=tk.W)

        tree.bind('<<TreeviewSelect>>', self.item_selected)
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

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            path = 'p3\downloads\\'
            if(not self.tree.parent(selected_item)):
                if(os.path.isfile(path+item['text']+'.zip')):
                    pass
                else:
                    filename = wget.download(str(record[0]), out = path+item['text']+'.zip')
                    with zipfile.ZipFile(filename, 'r') as zip:
                        zip.extractall(path=path)
                id = 0
                ch = 0
                for child in self.tree.get_children():
                    if item['text'] in self.tree.item(child)['text']:
                        pid = id
                    ch += len(self.tree.get_children([child]))
                    id+=1
                cd = len(self.tree.get_children()) + ch
                if not self.tree.get_children([pid]):
                    id = 0
                    for f in os.listdir(path+item['text']):
                        self.tree.insert('', tk.END, text=f.split('_')[4], iid=id+cd, open=False, values=f)
                        self.tree.move(id+cd, pid, id)
                        id+=1
            else:
                file = path + self.tree.item(self.tree.parent(selected_item))['text'] + '\\' + (" ").join(record)
                self.create_graph_widget(file)
    
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

    def create_graph_widget(self, file):
        fig = Figure(figsize=(5,4), dpi=100)
        ax = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        df = pd.read_csv(file, encoding='iso-8859-1', decimal=',', delimiter=';', skiprows=8)
        index = pd.DatetimeIndex(df.iloc[:, 0], name='Data')
        df.drop(columns=df.columns[0], axis=1, inplace=True)
        df.set_index(index, inplace=True)
        df['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'] = df['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].apply(lambda x : None if x < -20 else x)
        temp = df.groupby(df.index)['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].mean()
        temp.index = temp.index.strftime("%b")
        temp.plot(ax=ax, title="Temperatura", ylabel="(°C)")
        df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].apply(lambda x : None if x < 0 else x)
        prec = df.groupby(df.index)['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].mean()
        prec.index = prec.index.strftime("%b")
        prec.plot(ax=ax2, title="Precipitação", ylabel="(mm)")
        fig.subplots_adjust(wspace=1, hspace=1)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().grid(row=0, column=1)
        
    def close_window(self):
        path = 'p3\downloads\\'
        arq = os.listdir(path)
        for file in arq:
            if os.path.isfile(path + file):
                os.remove(path + file)
            if os.path.isdir(path + file):
                shutil.rmtree(path + file)
        self.destroy()
     
