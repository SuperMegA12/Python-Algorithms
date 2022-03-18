import random
vetor = []
for c in range(0,4):
    alunos = str(input(f'Digite o nome do {c+1}ª aluno:')).strip()
    vetor.append(alunos)
random.shuffle(vetor)
print(f'A ordem é {vetor}')