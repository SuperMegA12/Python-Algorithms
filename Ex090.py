dicionario = {}
dicionario["Nome"] = str(input('NOME: '))
dicionario["Média"] = float(input('Média: '))
print(f'O nome é: {dicionario["Nome"]}')
print(f'A sua média é: {dicionario["Média"]}')
if dicionario["Média"]  < 5:
    print('Reprovado!')
elif dicionario["Média"] >= 5 and dicionario["Média"] < 7:
    print('Recuperação!')
else:
    print("Aprovado!!!")

print(dicionario)


#Ex090 - Dicionário em Python

