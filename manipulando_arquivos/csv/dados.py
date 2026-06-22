import csv
import os

PASTA = "arquivos"
CAMINHO_ARQUIVO = os.path.join(PASTA, "biblioteca.csv")
CAMPOS = ["isbn", "titulo", "autor", "genero", "ano_publicacao", "editora", "paginas", "status", "localizacao"]

def inicializar_diretorio():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def salvar_no_arquivo(lista_dados):
    inicializar_diretorio()
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()  # Escreve a primeira linha (nomes das colunas)
        escritor.writerows(lista_dados) # Escreve todos os livros

def carregar_do_arquivo():
    if os.path.exists(CAMINHO_ARQUIVO):
        biblioteca_aux = []
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                linha['ano_publicacao'] = int(linha['ano_publicacao']) if linha['ano_publicacao'] else 0
                linha['paginas'] = int(linha['paginas']) if linha['paginas'] else 0
                biblioteca_aux.append(linha)
        return biblioteca_aux
    return []