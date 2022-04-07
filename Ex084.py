lista = []
dados = []
menor = maior = 0

while True:
    dados.append (str(input('Nome: ')))
    dados.append (float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    pergunta = str(input('Continuar [S/N]: ')).strip().upper()
    if pergunta !='S':
        break



print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maior} KG. De ', end='')
for p in lista:
    if p[1] == maior:
        print(f'({p[0]}) ', end='')
print()
print(f'O menor peso foi de {menor} KG. De ', end='')
for p in lista:
    if p[1] == menor:
        print(f'({p[0]}) ', end='')
print()



#Ex084 - Lista composta e análise de dados



