from flask import Flask, jsonify, request

app_music = Flask(__name__)
musicas = [
    {
        'musica': 'Milu',
        'estilo': 'Sertanejo'
    },
    {
        'musica': 'TNT',
        'estilo': 'Rock'
    },
    {
        'musica': 'Cheia de Manias',
        'estilo': 'Samba'
    },
    {
        'musica': 'Just be it',
        'estilo': 'Pop'
    },
    {
        'musica': 'The Reason',
        'estilo': 'Lyrics'
    }
]

# Listar músicas - GET http://localhost:5000
@app_music.route('/')
def consultar_musicas():
    return jsonify(musicas)

# Consultar uma música por índice - GET Id http://localhost:5000/musicas/1
@app_music.route('/musicas/<int:indice>', methods=['GET'])
def consultar_musica_por_indice(indice):
    return jsonify(musicas[indice])

# Editar músicas existentes - PUT http://localhost:5000/musicas/1
@app_music.route('/musicas/<int:indice>', methods=['PUT'])
def editar_musica(indice):
    musica_editada = request.get_json()
    musicas[indice].update(musica_editada)

    return jsonify(musicas[indice], 200)

# Excluir uma música - DELETE http://localhost:5000/musicas/1
@app_music.route('/musicas/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Música excluída {musicas[indice]}', 200)
    except:
        return jsonify(f'Música não encontrada', 404)

# Inserir uma nova música - POST  http://localhost:5000/musicas
@app_music.route('/musicas', methods=['POST'])
def inseri_nova_música():
    nova_musica = request.get_json()
    musicas.append(nova_musica)

    return jsonify(nova_musica, 200)

app_music.run(port=5000, host='localhost', debug=True)
