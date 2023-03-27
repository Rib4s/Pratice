# DESAFIO - Criar um arquivo JSON
# Exercício para criação de arquivo JSON do curso Mestre Pythonista na Dev Aprender com o instrutor Jhonatan
import json
# 1- criar uma string formatada como json
criar_string_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""
# 2- Salvar a string como arquivo json
with open('desafio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(criar_string_json, arquivo_json)
