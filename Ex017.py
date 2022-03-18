import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hipot = math.hypot(co,ca)
print(f'O valor da hipotenusa é {hipot:.2f}')