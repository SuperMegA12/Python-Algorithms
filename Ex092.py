from datetime import date
dicionario = {}
dicionario["Nome"] = str(input('NOME: '))
dicionario["Ano de nascimento"] = int(input('ANO DE NASCIMENTO: '))
dicionario["Idade"] = date.today().year - dicionario["Ano de nascimento"]
dicionario["Carteira de trabalho"] = int(input('NÚMERO da Carteira de Trabalho (0 não tem): '))
if dicionario["Carteira de trabalho"] > 0:
    dicionario["Ano de contratação"] = int(input('ANO DE CONTRATAÇÃO: '))
    dicionario["Salário"] = float(input('SALÁRIO R$: '))
    dicionario["Idade"] = date.today().year - dicionario["Ano de nascimento"]
    dicionario["Aposentadoria"] = 53
    print('=-'*30)
    for k, v in dicionario.items():
        print(f'{k} tem valor de {v}')
        print('-'*30)
else:
    print('=-'*30)
    print(f"Nome tem valor de {dicionario['Nome']}")
    print(f"Idade tem valor de {dicionario['Idade']}")
    print('Não tem carteira de trabalho')




#Ex092 - Cadastro de Trabalhador em Python




