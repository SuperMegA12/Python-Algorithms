dicionario = {}
acima_media = {}
lista_nomes = []
mulheres = []
idade = []
galera = []
soma = media = 0
while True:
    dicionario.clear()
    dicionario["Nome"] = str(input('Nome: ')).strip().upper()
    while True:

        dicionario["Sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dicionario["Sexo"] == 'F':
            mulheres.append(dicionario["Nome"])

        if dicionario["Sexo"] in "MF":
            break
        print('Inválido, digite apenas M OU F.')


    dicionario["Idade"] = int(input('Idade: '))
    soma+=dicionario["Idade"]
    galera.append(dicionario.copy())


    while True:
        pergunta = str(input('Continuar [S/N]: ')).strip().upper()[0]
        if pergunta in 'SN':
           break
        print('Inválido. Responda apenas S OU N.')
    if pergunta == 'N':
        break

print('=-'*30)

print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')

media = soma / len(galera)

print(f'B) A média de idade é {media:.2F}')

print('C) As mulheres cadastradas foram:', end=' ')
for mulher in mulheres:
    print(f'{mulher} |', end=' ')


print('\nD) Pessoas com idade acima da média: ')

for p in galera:
    if p['Idade'] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()


print('<<<ENCERRANDO>>>>')



#Ex094 - Unindo dicionários e listas
















#dicionario["Nome"] = lista[:]
#dicionario["Sexo"] = lista[:]
#dicionario["Idade"] = lista[:]


