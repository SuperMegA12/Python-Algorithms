lista = []
lis_man = []
cont_woman = 0
for c in range(1,5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª pessoa:'))
    lista.append(idade)
    sexo = str(input(f'Digite o sexo da {c}ª pessoa [M/F]:')).upper().strip()
    if sexo == 'M':
        lis_man.append(nome) and lis_man.append(idade)
    if sexo == 'F' and idade < 20:
        cont_woman+= 1
    print('=-='*20)
media = (lista[0] + lista[1]+ lista[2] + lista[3]) / 4
homen_velho = max(lis_man)
print(f'A média de idade do grupo é de {media:.0f} anos')
print(f'O nome do homen mais velho é {homen_velho}.')
print(f'Ha {cont_woman} mulheres menores de 20 anos.')


