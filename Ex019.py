import random
vetor= []
for c in range(0,4):
    aluno = str(input(f'Digite o nome do {c+1}ª aluno :')).strip()
    vetor.append(aluno)
escolhido = random.choice(vetor)
print(f'O aluno escolhido para apagar o quadro foi {escolhido}')