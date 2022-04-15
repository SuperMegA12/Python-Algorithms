from random import randint
from time import sleep
from operator import itemgetter
lista = []
dic = {"Jogador1": randint(1,6), "Jogador2": randint(1,6), "Jogador3": randint(1,6),"Jogador4":randint(1,6)}
ranking = list
print('VALORES SORTEADOS')
for k, v in dic.items():
    print(f'O {k} tirou {v} tirou no dado')
    sleep(1)

ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)

print('=-'*20)
print('== RANKING DOS JOGADORES == ')

for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)


