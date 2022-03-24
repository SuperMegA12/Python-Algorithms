cont_1 = 0
cont_2 = 0
soma = 0
n = int(input('Digite um número:'))
soma+=n
cont_1+=1
while n !=999:
    n = int(input('Digite outro número: '))
    cont_2+=1
    soma += n
    if n == 999:
        cont_2-=1
        soma-=n
        break
print(f'Você digitou {cont_1+cont_2} valores. E a soma deles corresponde a {soma}')



#Ex064 - Tratando vários Valores
