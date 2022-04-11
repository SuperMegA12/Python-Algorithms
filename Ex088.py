from random import randint
from time import sleep
cont = 0
print('-='*30)
print('                    JOGO NA MEGA SENA')
print('-='*30)
n = int(input('Quantos jogos você quer que eu sortei?: '))
for i in range(n):
    lista = []
    for valores in range (6):
        sorteio = randint(0,60)
        if sorteio in lista:
            sorteio = randint(0,60)
            lista.append(sorteio)
        else:
            lista.append(sorteio)


    print(f'{i+1}ª JOGO: {lista}')
    sleep(0.5)

print('BOA SORTE')



#Ex088 - Palpites para a Mega Sena



