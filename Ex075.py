cont = pares = 0
tupla = ()
transformando = list(tupla)
for c in range(0,4):
    n = int(input('ENTER A VALUE : '))
    transformando.append(n)
    if n == 9:
        cont+=1
tupla = tuple(transformando)
print(f'O valor 9 apareceu {cont} vez(es).')
print(f'O valor 3 apareceu pela primeira vez na posição {tupla.index(3)}')
print(f'Os valores pares digitados foram:', end='')
for np in tupla:
    if np % 2 ==0:
        print( np , end=' ')
