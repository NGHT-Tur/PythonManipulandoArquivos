from flask import Flask, jsonify, request
import dados

biblioteca = dados.carregar_do_arquivo()

app = Flask(__name__)

@app.route('/biblioteca')
@app.route('/biblioteca/<isbn>')
def detalhar_livro (isbn=None):
    if isbn None:
        return jsonify(biblioteca)
    else:
        for livro in biblioteca:
            if livro['isbn'] == isbn:
        return jsonify(livro)
    return jsonify("Livro não encontrado"), 404

@app.route('/biblioteca/criar', methods=['POST'])
def cria_livro():
    novo_livro = request.get_json()
    biblioteca.append(novo_livro)
    dados.salvar_no_arquivo (biblioteca)
    return jsonify("Livro criado com sucesso"), 201

@app.route('/biblioteca/deletar/<isbn>', methods=['DELETE'])
def deleta_livro(isbn=None):
    for livro in biblioteca: 
        if livro['isbn'] == isbn:
            biblioteca.remove(livro)
            dados.salvar_no_arquivo(biblioteca)
            return jsonify("Livro deletado com sucesso"), 200

@app.route('/biblioteca/update/<isbn>', methods=['PUT'])
def altera_livro(isbn=None):
    novo_livro = json.load(request.get_json())
    for livro in biblioteca: 
        if livro['isbn'] == isbn:
            for key, value in novo_livro:
                livro[key] = value
            dados.salvar_no_arquivo(biblioteca)
            return jsonify("Livro alterado com sucesso"), 200
    return "Estamos trabalhando nisso"
           
if __name__ '_main__':
    app.run()