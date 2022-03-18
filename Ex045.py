from random import randint
jogada = int(input('''QUAL SUA JOGADA?
    PEDRA   [0]
    PAPEL   [1]
    TESOURA [2]
    
    DIGITE O NÚMERO :'''))
computador = randint(0,2)
if jogada == 0:
    print(f'Você jogou Pedra')
    if computador  == 0:
        print(f'O computador também jogou Pedra. EMPATE!!!')
    if computador == 1:
        print(f'O computador jogou Papel. DERROTA!!!')
    if computador == 2:
        print(f'O computador jogou Tesoura. VITÓRIA!!!')
elif jogada == 1:
    print('Você jogou Papel')
    if computador  == 0:
        print(f'O computador também jogou Pedra. DERROTA!!!')
    if computador == 1:
        print(f'O computador jogou Papel. EMPATE!!!')
    if computador == 2:
        print(f'O computador jogou Tesoura. VITÓRIA!!!')
elif jogada == 2:
    print('Você jogou Tesoura')
    if computador  == 0:
        print(f'O computador também jogou Pedra. DERROTA!!!')
    if computador == 1:
        print(f'O computador jogou Papel. VITÓRIA!!!')
    if computador == 2:
        print(f'O computador jogou Tesoura. EMPATE!!!')
while jogada > 2 or jogada < 0:
    jogada = int(input('''OPÇÃO INVÁLIDA. QUAL SUA JOGADA?
    PEDRA   [0]
    PAPEL   [1]
    TESOURA [2]

    DIGITE O NÚMERO :'''))
    computador = randint(0, 2)
    if jogada == 0:
        print(f'Você jogou Pedra')
        if computador == 0:
            print(f'O computador também jogou Pedra. EMPATE!!!')
        if computador == 1:
            print(f'O computador jogou Papel. DERROTA!!!')
        if computador == 2:
            print(f'O computador jogou Tesoura. VITÓRIA!!!')
    elif jogada == 1:
        print('Você jogou Papel')
        if computador == 0:
            print(f'O computador também jogou Pedra. DERROTA!!!')
        if computador == 1:
            print(f'O computador jogou Papel. EMPATE!!!')
        if computador == 2:
            print(f'O computador jogou Tesoura. VITÓRIA!!!')
    elif jogada == 2:
        print('Você jogou Tesoura')
        if computador == 0:
            print(f'O computador também jogou Pedra. DERROTA!!!')
        if computador == 1:
            print(f'O computador jogou Papel. VITÓRIA!!!')
        if computador == 2:
            print(f'O computador jogou Tesoura. EMPATE!!!')
