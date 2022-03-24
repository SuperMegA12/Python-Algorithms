lista = []
for c in range(1,6):
  peso = float(input(f'Digite o peso da {c}ª pessoa: KG'))
  lista.append(peso)
maior = max(lista)
menor = min(lista)

print(f'O maior peso registrado foi {maior}KG . E o menor peso registrado foi {menor} KG')



#Ex055 - Maior e Menor da sequência