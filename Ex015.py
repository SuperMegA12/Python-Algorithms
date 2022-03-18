km_rodados = int(input('Digite a quantidade de KM rodados: KM'))
dias = int(input('Por quantos dias ele foi alugado? :'))
custo_km = km_rodados * 0.15
custo_dias = dias * 60
print(f'O custo dos dias alugados é de {custo_dias} e de KM rodados é de {custo_km:.2f}')
print(f'TOTAL A PAGAR {custo_dias + custo_km} R$')
