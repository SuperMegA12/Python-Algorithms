n = int(input('Digite qualquer número com 4 dígitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Unidade {u}. Dezena {d}. Centena {c}. Milhar {m}.')