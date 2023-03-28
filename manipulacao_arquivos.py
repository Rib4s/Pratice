''' Curso: Mestre Pythonista - Dev Aprender
    Instrutor: Jhonatan '''

# 🥇 DESAFIO Manipulação de Arquivos🥇
# Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
import os

# Primeiro crie 3 listas:
# * Uma lista que contem 5 frutas
frutas = ['Laranja', 'Maçã', 'Banana', 'Pêssego', 'Abacaxi']
# * Uma lista que contem 5 cores
cores = ['Vermelho', 'Azul', 'Amarelo', 'Verde', 'Branca']
# * Uma lista que contem 5 linguagens de programação
linguagens = ['Python', 'C#', 'Javascript', 'Java', 'C++']

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open('frutas.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt', 'r', encoding='utf-8') as arquivo_frutas:
    for fruta in arquivo_frutas:
        print(fruta)

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt', 'r+', encoding='utf-8', newline='') as frutas_cores:
    for linha in frutas_cores:
        for cor in cores:
            frutas_cores.write(cor + os.linesep)

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linguagem ocupe apenas uma linha.
with open('Top 5 Linguagens.txt', 'w', encoding='utf-8', newline='') as arquivo_linguagens:
    for linguagem in linguagens:
        arquivo_linguagens.write(linguagem + os.linesep)

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
contador = 1
qtde_arquivos = 5 * ' '
for arquivo in qtde_arquivos:
    with open(f'Arquivo{contador}.txt', 'w') as criar_arquivo:
        contador += 1
