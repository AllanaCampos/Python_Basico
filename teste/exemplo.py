import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from bs4 import BeautifulSoup
import requests
import wget
import zipfile

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        tree = ttk.Treeview(self)
        tree.heading('#0', text='Anos', anchor=tk.W)

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NSEW)

        # generate sample data
        ano, link = self.getAnos()
        id = 0
        for i in ano:
            tree.insert('', tk.END, text=i.split(' ')[1], iid=id, open=False, values=link[id])
            id+=1

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            path = 'teste/downloads/'
            filename = wget.download(str(record[0]), path+item['text']+'.zip')
            
            with zipfile.ZipFile(filename, 'r') as zip:
                zip.extractall()
            #self.tree.insert('', tk.END, text=i.split(' ')[1], iid=id, open=False, values=link[id])
            # show a message
            showinfo(title='Information', message=record)
    
    def getAnos(self):
        url = 'https://portal.inmet.gov.br/dadoshistoricos'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        requisicao = requests.get(url, headers=headers)

        texto = BeautifulSoup(requisicao.text, 'html.parser')
        articles = texto.find_all('article')
        ano =  []
        link = []
        for i in articles:
            ano.append(i.find('a').string)
            link.append(i.find('a')['href'])
            #print(i.find('a')['href'])
            #wget.download(link[-1], ano[-1]+'.zip')
        return ano, link



if __name__ == '__main__':
    app = App()
    app.mainloop()
     
