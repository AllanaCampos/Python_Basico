import tkinter as tk

root = tk.Tk()
root.title("Exemplo 13")
l1 = tk.Frame(root).pack(side = tk.TOP)
l2 = tk.Frame(root).pack(side = tk.TOP)
l3 = tk.Frame(root).pack(side = tk.TOP)

texto = tk.StringVar()


label = tk.Label(l1,text=texto.get()).pack(side=tk.LEFT,anchor=tk.N)

entry = tk.Entry(l1,textvariable=texto).pack(side = tk.LEFT)

def pegaTexto():
    print(texto.get())

def limpaTexto():
    texto.
    

b1 = tk.Button(l2,text="B1",command=pegaTexto).pack(side=tk.LEFT,anchor=tk.N)
b2 = tk.Button(l2,text="B2",command=limpaTexto).pack(side = tk.LEFT)
sair = tk.Button(l3,text="Sair",command=root.quit).pack()

root.mainloop()