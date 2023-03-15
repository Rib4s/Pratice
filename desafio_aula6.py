# Desafio 🥇
''' Crie um dacorator que irá pegar a função que for passado para ele e imprimir o horário
atual antes de executar a função e depois imprimir o horário após ter finalizado a execução da função.
    • Dica: você terá que usar o módulo datetime para conseguir o horério atual.'''

from datetime import datetime


def horario_cadastro(funcao):
    def horario():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return horario


@horario_cadastro
def cadastrar():
    print('Cadastro realizado com sucesso!')


cadastrar()
