lista = []

c = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    c += 1
    pergunta = str(input('Continuar [S/N]: ')).strip().upper()
    if pergunta != 'S':
        break

print(f'Foram digitados {c} valores.')
if 5 in lista:
    print(f'O número 5 está na lista. Na posição {lista.index(5)}')
else:
    print('Valor 5 não encontrado!!')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}')



#Ex081 - Extraindo dados de uma Lista

