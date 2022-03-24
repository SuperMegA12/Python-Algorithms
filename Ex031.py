dist = float(input('De quantos KM foi a viagem? : KM/H '))
smaller_price = 0.50 * dist
if dist > 200:
     bigger_price = 0.45 * dist
     print(f'O preço da sua viagem será de {bigger_price:.2f}R$')
else:
    print(f'O preço da sua viagem  será de {smaller_price:.2f}R$')




#Ex031 - Custo da Viagem
