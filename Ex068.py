
from random import randint

cont = 0
print('=-='*15)
print('          VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*15)
computador = randint(0,10)


while True :

    jogada = str(input('[P/I]: ')).strip().upper()
    if jogada != 'P' and jogada != 'I':
        print('Alternativa inválida. Recomece o jogo')
        break
    n = int(input('Qual número entre 0 a 10 você quer jogar?: '))
    if n < 0 or n > 10:
        print('Número inválido. Recomece o jogo')
        break
    soma = computador + n

    if soma % 2 == 0:
        print(f'Você jogou {n} e eu joguei {computador}. A soma é {soma} esse número é PAR')
        if jogada == 'P':
            print('Você ganhou!!')
            cont+=1
        elif jogada == 'I':
            print('Você perdeu!!')
            break
    elif soma % 2 == 1:
        print(f'Você jogou {n} e eu joguei {computador}. A soma é {soma} esse número é ÍMPAR')
        if jogada == 'I':
            print('Você ganhou!!')
            cont+=1
        elif jogada == 'P':
            print('Você perdeu!!')
            break
print(f'Você teve um total de {cont} vitórias!!')



#Ex068 - Jogo Par ou Ímpar
