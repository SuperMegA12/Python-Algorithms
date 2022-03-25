list = []
cont = soma  = 0
barato =''
while True:
    nome = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço do produto: R$ '))
    soma+=price
    list.append(price)
    if price > 1000:
        cont+=1
    menor = min(list)
    if price == menor:
        barato = nome
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper() [0]
    if continua == 'N':
        break
print(f'''O total gasto na compra foi de {soma} R$. 
Ha {cont} produto(s) mais caro(s) que 1000R$. 
E o produto mais barato custa é o {barato} custando {menor} R$''')



#Ex070 - Estatísticas em Produto