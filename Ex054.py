from datetime import date
cont_maior = 0
cont_menor = 0
data_atual = date.today().year
for c in range(1,8):
    data_nascimento = int(input(f'Digite a data de nascimento da {c}ª pessoa: '))
    data = data_atual - data_nascimento
    if data >= 18:
        cont_maior+=1
    elif data < 18:
        cont_menor+=1
    print('=-='*20)
print(f'Ha {cont_maior} pessoas de maior idade \nHa {cont_menor} pessoas de menor idade')