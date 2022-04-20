dados = {}
partidas = []
time = []
while True:
    dados.clear()
    dados["Nome"] = str(input('Nome do jogador: '))
    dados["Partidas jogadas"] = int(input(f'Quantas partidas o jogador {dados["Nome"]} jogou? : '))
    partidas.clear()
    for c in range(dados["Partidas jogadas"]):
        partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida? : ')))
    dados["Gols"] = partidas[:]
    dados["Total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        pergunta = str(input('Continuar [S/N]: ')).strip().upper()[0]
        if pergunta in 'SN':
            break
        print('Inválido. Responda apenas S OU N.')
    if pergunta == 'N':
        break
print('-='*30)
print('cod', end='')
for i in dados.keys():
    print(f'{i:<15} ', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca > len(time):
        print('Código de busca inválido.')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'  No jogo {i+1} fez {g} gol(s)')
    print('-'*40)
print('<<<<<VOLTE SEMPRE>>>>>>')



#Ex95 - Aprimorando os Dicionários
