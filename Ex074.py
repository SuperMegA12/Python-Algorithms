from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os valores sorteados foram:', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(numeros)}')
print(f'E o menor é {min(numeros)}')



#Ex074 -  Maior e Menor valor em Tupla