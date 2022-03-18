from random import randint
cont = 0
cont_2 = 0
computador = randint(0,10)
pergunta = int(input('Advinhe o número que eu estou pensando. Chute um número de 1 a 10: '))
cont_2+=1
while pergunta != computador:
    pergunta = int(input('Errou, tente novamente. Advinhe o número que eu estou pensando. Chute um número de 1 a 10: '))
    cont+=1
    if pergunta == computador:
        print(f'''Parabéns! Eu pensei no número {computador}, e você chutou o mesmo número! Somos iguais.
você acertou após {cont_2+cont} tentativas.''')
