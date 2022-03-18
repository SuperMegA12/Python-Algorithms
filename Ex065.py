list = []
soma = 0
cont = 0
n = float(input('Digite um valor inteiro: '))
soma+=n
cont+=1
list.append(n)

pergunta = str(input('Desja continuar? [S/N]: ')).strip().upper()
while pergunta == 'S':
    n = float(input('Digite um valor inteiro: '))
    cont+=1
    soma+=n
    list.append(n)
    pergunta = str(input('Desja continuar? [S/N]: ')).strip().upper()
maior = max(list)
menor = min(list)
media = soma/cont
print(f'O maior valor digitado foi {maior} e o menor foi {menor} . E a média dos valores digitados é {media:.2f} ')



