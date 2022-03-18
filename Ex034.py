wage = float(input('Digite o seu salário: R$'))
if wage >= 1250:
    print(f'O seu aumento será de 10%. O valor de {wage:.2f}R$ MAIS 10% é de {wage + (wage * 10/100):.2f}R$')
else:
    print(f'O aumento será de 15%. O valor de {wage:.2f}R$ MAIS 15% é de {wage + (wage * 15/100):.2F}R$ ')