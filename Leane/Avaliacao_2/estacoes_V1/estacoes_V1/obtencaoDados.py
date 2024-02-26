import wget 

class ObterDados:
    
     def downloadDados(self, anoSelecionado, anos):
        link = None
        for ano in anos:
            if ano[0] == anoSelecionado:
                link = ano[1]
                wget.download(link, f'csvs/{anoSelecionado}.zip')

        if link is None:
            print(f"Não foi possível encontrar o link para o ano {anoSelecionado}")