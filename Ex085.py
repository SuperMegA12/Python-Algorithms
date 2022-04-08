valores = [[],[]]
for c in range(0,7):
    valores = int(input(f'Digite o {c+1}ª valor: '))
    if valores % 2 == 0:
        valores[0].append(valores)
    else:
       valores[1].append(valores)



print(f'Valores pares {sorted(valore[0])}')
print(f'Valores ímpares {sorted(valores[1])}')




#Ex085 = Listas com Pares e Ímpares