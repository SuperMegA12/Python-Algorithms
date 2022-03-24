numero = int(input('Digite um número inteiro para saber sua tabuada:'))
valor_saber = int(input('Até qual valor você deseja saber a tabuada? :'))
for cont in range (valor_saber):
    print( f'{numero} X {cont+1} = {numero * (cont+1)}')



#Ex049 - Tabuada v2.0