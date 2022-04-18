somador = 0
dados = {}
partidas = []
dados["Nome"] = str(input('Nome do jogador: '))
dados["Partidas jogadas"] = int(input(f'Quantas partidas o jogador {dados["Nome"]} jogou? : '))
for c in range(dados["Partidas jogadas"]):
    partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida? : ')))
dados["Gols"] = partidas[:]
dados["Total"] = sum(partidas)
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])}')
for i, v in enumerate(dados["Gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gol(s).')



#Ex93 - Cadastro de Jogador de Futebol



