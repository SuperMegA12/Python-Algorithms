ficha = []
lista_notas = []
lista_media = []
cont = 0
while True:
    nome = str(input('Nome: ')).strip().upper()
    nota_1 = float(input('1ª Nota: '))
    nota_2 = float(input('2ª Nota: '))
    media = (nota_1+nota_2)/2
    ficha.append([nome, [nota_1, nota_2], media])
    pergunta = str(input('CONTINUAR [S/N]: ')).strip().upper()
    if pergunta != 'S':
        break

print('=-='*30)
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
print('-' * 26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    print('VOLTE SEMPRE')



#EX089 - Boletim com Listas Compostas



