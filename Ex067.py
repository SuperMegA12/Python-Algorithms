numero = ''
while numero != -1:
    numero = int(input('Digite um número inteiro para saber sua tabuada:'))
    if numero < 0:
        break
    valor_saber = int(input('Até qual valor você deseja saber a tabuada? :'))
    for cont in range (valor_saber):
        print( f'{numero} X {cont+1} = {numero * (cont+1)}')
print('FIM')
