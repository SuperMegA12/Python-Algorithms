num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
     print('\033[34m', end=' ')
     tot+=1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m O número {num} foi dividido {tot} vezes.')
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')



#Ex052 - Números primos