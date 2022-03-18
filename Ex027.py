nome = str(input('Digite seu primeiro e segundo nome: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]} e seu último nome é {n[len(n) - 1]}')