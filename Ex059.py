loop = ''
list = []
valor_1 = float(input('1ª VALOR: '))
list.append(valor_1)
valor_2 = float(input('2ª VALOR: '))
list.append(valor_2)
maior = max(list)
while loop == '':
    print('''             [1] SOMAR
             [2] MULTIPLICAR
             [3] MAIOR VALOR
             [4] NOVOS NÚMEROS
             [5] SAIR DO PROGRAMA''')

    option = int(input('>>>>>>> Qual sua opção de operação? : '))
    if option == 1:
        print(f'{valor_1:} + {valor_2:} = {valor_1 + valor_2}')
    elif option == 2:
        print(f'{valor_1} x {valor_2:} = {valor_1 * valor_2}')
    elif option == 3:
        print(f'O maior valor entre {valor_1} e {valor_2} é {maior}')
    elif option == 4:
        list.clear()
        valor_1 = float(input('1ª VALOR: '))
        list.append(valor_1)
        valor_2 = float(input('2ª VALOR: '))
        list.append(valor_2)
    elif option == 5:
        print('Volte sempre para mais cálculos')
        break
    elif option < 1 or option > 5:
        print('OPÇÃO INVÁLIDA. ESCOLHA UMA OPÇÃO CORRESPONDENTE.')



#Ex059 - Criando um Menu de Opções



