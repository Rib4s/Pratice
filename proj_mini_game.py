from turtle import Turtle

t = Turtle()
t.speed(1)
while True:
    direcao = input('Qual direção devemos ir? "f:frente" ou "t:trás"? ')
    if direcao == 'f':
        distancia = int(
            input('Quantos pixels devemos movimentar para frente? '))
        rotacao = input(
            'Rotacionar para d:direita, e:esquerda ou n:não rotacionar? ')
        if rotacao == 'd':
            dir = int(input('Quantos para a direita devemos rotacionar? '))
            t.right(dir)
            t.forward(distancia)
        elif rotacao == 'e':
            esq = int(input('Quantos para a esquerda devemos rotacionar? '))
            t.left(esq)
            t.forward(distancia)
        elif rotacao == 'n':
            t.forward(distancia)
    elif direcao == 't':
        distancia = int(input('Quantos pixels devemos movimentar para trás? '))
        rotacao = input(
            'Rotacionar para d:direita, e:esquerda ou n:não rotacionar? ')
        if rotacao == 'd':
            dir = int(input('Quantos para a direita devemos rotacionar? '))
            t.right(dir)
            t.backward(distancia)
        elif rotacao == 'e':
            esq = int(input('Quantos para a esquerda devemos rotacionar? '))
            t.left(esq)
            t.backward(distancia)
        elif rotacao == 'n':
            t.backward(distancia)
    terminar = input('Continuar andando? ')
    if terminar == 's':
        continue
    else:
        break
