import wget
import zipfile
import os

class DownloadDados:

    def downloadDados(self, anoSelecionado, anos):
        link = None
        for ano in anos:
            if ano[0] == anoSelecionado:
                link = ano[1]
                if  not anoSelecionado+".zip" in os.listdir('csvs'):
                    wget.download(link, f'csvs/{anoSelecionado}.zip')
        
        caminho = f'csvs/{anoSelecionado}.zip'
        with zipfile.ZipFile(caminho, 'r') as zip_ref:
            zip_ref.extractall(f'csvs')
            titulosArquivos = zip_ref.namelist()
            
            nomesCidades = []
            
            for titulo in titulosArquivos:
                partes = titulo.split('_')
                if len(partes) >= 5:
                    cidade = partes[4]
                    nomesCidades.append(cidade)

        if link is None:
            print(f"Não foi possível encontrar o link para o ano {anoSelecionado}")
            
        return nomesCidades, titulosArquivos
