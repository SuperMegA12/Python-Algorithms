from datetime import date
data_nascimento = int(input('Qual ano você nasceu? : '))
data_atual = date.today().year
idade = data_atual - data_nascimento
if idade >= 5 and idade <=9:
    print(f'Você tem {idade} anos. Você é um atleta mirim.')
elif idade >=10 and idade <=14:
    print(f'Você tem {idade} anos. Você é um atleta infantil.')
elif idade >= 15 and idade <=19:
    print(f'Você tem {idade} anos. Você é um atleta junior.')
elif idade >= 20 and idade <= 25:
    print(f'Você tem {idade} anos. Você é um atleta senior.')
elif idade >=25 and idade <=45:
    print(f'Você tem {idade} anos. Você é um atleta master.')
else:
    print(f'Com essa idade de {idade} anos, não é possível participar como atleta.')