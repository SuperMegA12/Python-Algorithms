lista = []
for c in range(0,5):
    value = int(input(f'Digite um valor para posição {c}: '))
    lista.append(value)
maior = max(lista)
menor = min(lista)
print('='*30)
print(f'Os valores digitados foram {lista}')
print(f'\nO maior valor foi {maior}. Digitado na posição: ', end='')
for i, v in enumerate (lista):
    if v == maior:
        print(f'{i}... ', end=' ')
print(f'\nO menor valor foi {menor}. Digitado na posição: ', end='')
for i, v in enumerate (lista):
    if v == menor:
        print(f'{i}...', end=' ')



#Ex078 - Maior e Menor valores na lista


