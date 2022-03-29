#O código antes da linha 8 é só para uma praticidade de adiconar os nomes.
tupla = ()
transformando = list(tupla)
for c in range(0,20):
    n = str(input(f'{c+1}ª COLOCADO: ')).strip().upper()
    transformando.append(n)
tupla = tuple(transformando)

##############################
alfabetico = sorted(tupla)
chape = 'CHAPECOENSE'
print(f'Os cinco primeiros são {tupla[0:5]} ')
print(f'Os quatro últimos colocados são {tupla[-4:]}')
print(f'Os times em ordem alfabética são {alfabetico}')
if chape in tupla:
    print(f'O time da Chapecoense está na posição {tupla.index(chape) + 1}ª')

#Ex073 - Tuplas com Times de Futebol
