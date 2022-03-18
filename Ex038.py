n = int(input('Digite o 1ª número: '))
n2 = int(input('Digite o 2ª número: '))
if n > n2:
    print(f'{n} é maior que {n2}')
elif n2 > n:
    print(f'{n2} é maior que {n}')
else:
    print('Não ha maior número')