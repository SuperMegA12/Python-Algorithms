lista = [[0,0,0],[0,0,0],[0,0,0]]
soma_coluna = 0
soma_pares = 0

for l in range(0,3):
    for c in range(0,3):
        lista[l][c]= int(input(f'Digite um valor para posição [{l}, {c}]: '))


print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista [l] [c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            soma_pares+=lista[l][c]
    print()
print(f'A soma de todos os pares digitados são {soma_pares}')
for l in range(0,3):
    soma_coluna+=lista[l][2]

print(f'A soma da terceira coluna é {soma_coluna}')

maior_segundaL = max(lista[1])
print('O maior valor da linha dois é ', maior_segundaL)



#Ex087 - Mais sobre Matrizes em Python


