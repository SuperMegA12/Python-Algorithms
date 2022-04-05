lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    for b in range(0, len(lista)):
        if n <= lista[b]:
            lista.insert(b, n)
            break
    if n not in lista:
        lista.append(n)
print(lista)



#Ex080 - Lista Ordenada sem repetições
