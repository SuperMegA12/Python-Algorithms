casa_valor = float(input('Qual o valor da casa? : R$'))
salario = float(input('Qual o valor do seu salário? : R$'))
anos = int(input('Em quantos anos você vai pagar? R$'))
anos_meses = anos * 12
prestacao = casa_valor / anos_meses
if prestacao > salario * 30/100:
    print(f'A prestação será de {prestacao}R$. Esse valor excede 30% do seu salário, portanto o empréstimo será negado.')
else:
    print(f'Empréstimo aprovado!')



#Ex036 - Aprovando Empréstimo
