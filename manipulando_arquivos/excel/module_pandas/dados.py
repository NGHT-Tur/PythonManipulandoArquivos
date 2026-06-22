import pandas as pd
import os

PASTA = "arquivos"
CAMINHO_ARQUIVO = os.path.join(PASTA, "biblioteca_pandas.xlsx")

def inicializar_diretorio():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def salvar_no_arquivo(lista_dados):
    inicializar_diretorio()
    df = pd.DataFrame(lista_dados)
    df.to_excel(CAMINHO_ARQUIVO, index=False, engine='openpyxl')

def carregar_do_arquivo():
    if os.path.exists(CAMINHO_ARQUIVO):
        df = pd.read_excel(CAMINHO_ARQUIVO, engine='openpyxl')
        return df.fillna('').to_dict(orient='records')
    return []