price = float(input('Qual o valor do produto? : R$'))
forma_pagamento = int(input('''Qual será a forma de pagamento?  
–  À vista dinheiro/cheque: 10% de desconto [1]
–  À vista no cartão: 5% de desconto        [2]
–  Em até 2x no cartão: preço formal        [3]
–  3x ou mais no cartão: 20% de juros       [4]

DIGITE O NÚMERO CORRESPONDEMTE A FORMA DE PAGAMENTO:'''))
while forma_pagamento == 0 or forma_pagamento > 4:
    forma_pagamento = int(input('''Qual será a forma de pagamento?  
    –  À vista dinheiro/cheque: 10% de desconto [1]
    –  À vista no cartão: 5% de desconto        [2]
    –  Em até 2x no cartão: preço formal        [3]
    –  3x ou mais no cartão: 20% de juros       [4]

    DIGITE O NÚMERO CORRESPONDEMTE A FORMA DE PAGAMENTO:'''))
if forma_pagamento == 1:
    print(f'Com o desconto você pagará {price - (price * 10/100)} R$')
elif forma_pagamento == 2:
    print(f'Com o desconto você pagará {price - (price * 5/100)} R$')
elif forma_pagamento == 3:
    print(f'Em 2x vezes no cartão você pagará 2 parcelas de {price/2}')
elif forma_pagamento == 4:
    metodo_4 = price + (price * 3 / 100)
    metodo_4_divisO = metodo_4 / 3
    print(f'Com o reajute dos juros você pagará 3 parcelas de {metodo_4_divisO}R$')