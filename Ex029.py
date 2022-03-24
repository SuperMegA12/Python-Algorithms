velocidade = int(input('Em qual velocidade estava o carro? : KM/h '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você ultrapassou o limite de 80KM. Sua multa será de {multa}R$')
else:
    print('Você está dentro do limite, dirija com cuidado.')



#Ex029 - Radar Eletrônico