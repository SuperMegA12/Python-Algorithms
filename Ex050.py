soma = 0
for c in range(0,7):
    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        soma = soma + n
print(soma)