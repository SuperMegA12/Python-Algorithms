r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmentto: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo.')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓLECES')
else:
    print('Não pode formar um triângulo')