r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmentto: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo.')
else:
    print('Não pode formar um triângulo')



#Ex035 - Analisando Triângulos v1.0