# DESAFIO JSON
# Exercício para leitura de arquivos JSON do curso Mestre Pythonista na Dev Aprender com o instrutor Jhonatan
import json

# Imprimir o e-mail do usuário com id 2
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])
    print('-'*100)

# imprimir a city do usuário com id 1
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][0]['address']['city'])
    print('-'*100)

# Imprimir o total do pedido do usuário com id 2
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['orders'][0]['total'])
