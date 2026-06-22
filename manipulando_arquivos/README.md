# 📚 Sistema de Gerenciamento de Biblioteca
Este projeto foi desenvolvido como material didático para a disciplina de Python. O objetivo é demonstrar a manipulação de dados em memória e a persistência em arquivos físicos (JSON e CSV), utilizando uma estrutura modularizada.

## 📂 Estrutura do Repositório
O repositório está dividido em duas abordagens de persistência:

/json: Versão que utiliza arquivos JavaScript Object Notation (JSON). Ideal para estruturas de dados complexas e aninhadas.

/csv: Versão que utiliza Comma-Separated Values (CSV). Ideal para dados tabulares e integração com planilhas (Excel/Sheets).

Cada pasta contém a mesma lógica de negócio, mas com implementações diferentes no módulo de dados:

main.py: Ponto de entrada do sistema (Menu).

funcoes.py: Lógica das operações (Cadastrar, Listar, Pesquisar, Alterar).

dados.py: Responsável por ler e escrever no disco.

arquivos/: Pasta onde os bancos de dados são gerados automaticamente.

## 🛠️ Funcionalidades
O sistema permite gerenciar o acervo completo de uma biblioteca com os seguintes campos:

- Identificação: ISBN (Chave única), Título, Autor e Editora.

- Classificação: Gênero, Ano de Publicação e Total de Páginas.

- Logística: Localização física (Estante/Prateleira) e Status (Disponível/Emprestado).

### Opções do Menu:
- Cadastrar: Adiciona um novo livro validando se o ISBN já existe.

- Listar: Exibe o acervo completo em formato resumido.

- Pesquisar: Busca detalhada por Título ou ISBN.

- Alterar: Permite editar qualquer campo de um livro já existente.

## 🎓 Conceitos de Programação Aplicados
Este projeto consolida os seguintes tópicos de estudo em Python:

1. ### Fundamentos e Estruturas de Dados
Dicionários (dict): Utilizados para representar cada livro como um objeto único.

Listas (list): Utilizadas para armazenar a coleção de livros em memória.

Manipulação de Strings: Uso de .strip(), .lower() e .upper() para tratar entradas do usuário.

2. ### Modularização
Divisão de Responsabilidades: Separação do código em múltiplos arquivos (.py), facilitando a manutenção e organização.

Importação de Módulos: Uso de import e nomes de escopo para acessar funções entre arquivos.

3. ### Processamento de Arquivos (I/O)
Context Managers (with): Abertura e fechamento seguro de arquivos.

#### JSON vs CSV:

Uso da biblioteca json para load e dump.

Uso da biblioteca csv com DictReader e DictWriter para manter a estrutura de dicionários.

Persistência: O ciclo de ler o arquivo, alterar na memória e sobrescrever o arquivo original.

4. ### Tratamento de Exceções
try/except: Implementado para evitar que o programa feche caso o usuário digite letras em campos numéricos (como Ano ou Páginas) ou caso o arquivo esteja corrompido.