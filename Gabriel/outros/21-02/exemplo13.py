import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Exemplo 13")

    textoEntry = tk.StringVar()
    textoLabel = tk.StringVar()

    tk.Label(
        root,
        textvariable=textoLabel).pack(
            side=tk.LEFT,
            expand=tk.YES,
            fill=tk.BOTH,
            anchor=tk.N)

    tk.Entry(
        root,
        textvariable=textoEntry).pack(
            side=tk.RIGHT,
            expand=tk.YES,
            fill=tk.BOTH,
            anchor=tk.N)
        
    tk.Button(
        root,
        text="B1",
        command=(lambda: textoLabel.set(textoEntry.get())),
        bg="green").pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH,
            anchor=tk.S)
    

    tk.Button(
        root,
        text="B2",
        command=(lambda: textoEntry.set("")),
        bg="blue").pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH,
            anchor=tk.S)
    
    tk.Button(
        root,
        text="Sair",
        command=root.quit,
        bg="red").pack(
            side=tk.BOTTOM,
            expand=tk.YES,
            fill=tk.BOTH)

    root.mainloop()


main()
