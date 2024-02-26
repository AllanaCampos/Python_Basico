import os
import zipfile
import wget 

class ObterDados:
    
     def downloadDados(self, anoSelecionado, anos):
        link = None
        for ano in anos:
            if ano[0] == anoSelecionado:
                link = ano[1]
                break  # Parar a busca se o ano for encontrado

        if link is None:
            print(f"Não foi possível encontrar o link para o ano {anoSelecionado}")
            return []  # Retorna uma lista vazia se o link não for encontrado

        caminho_zip = f'csv/{anoSelecionado}.zip'
        caminho_extracao = 'csv/'
        
        
        if not os.path.exists(caminho_extracao):
            os.makedirs(caminho_extracao)

        try:
            # Baixar o arquivo zip
            wget.download(link, caminho_zip)
            
            # Extrair o conteúdo do arquivo zip
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(caminho_extracao)
                titulos_arquivos = zip_ref.namelist()
            
            # Extrair nomes das cidades dos títulos dos arquivos
            nomes_cidades = [titulo.split('_')[4] for titulo in titulos_arquivos if len(titulo.split('_')) >= 5]

            return nomes_cidades
        except Exception as e:
            print(f"Erro ao baixar/descompactar arquivos: {e}")
            return []  # Retorna uma lista vazia em caso de erro