from datetime import date
data_nascimento = int(input('Qual ano você nasceu? : '))
data_atual = date.today().year
idade = data_atual - data_nascimento
if idade == 18:
    print('Você está no período certo de alistamento. Procure uma junta militar mais próxima.')
elif idade == 16:
    print('Na sua idade o alistamento é opcional. Caso deseje se alistar, vá a junta militar mais próxima.')
elif idade >= 19 or idade <=45:
    print('Caso você AINDA não tenha se alistado, deverá pagar uma multa de 30R$,e recorrer a uma junta mais próxima.')
