lista = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num
    if num % 2 == 0:
      lista_pares.append(num)
    else:
        lista_impares.append(num)
    question = str(input('Continuar [S/N]: ')).strip().upper()
    if question != 'S':
        break
print(f'Valores da lista com todos os números {lista}')
print(f'Valores da lista de números PARES {lista_pares}')
print(f'Valores da lista de números ÍMPARES {lista_impares}')



#Ex082 - Dividindo valores em Lista