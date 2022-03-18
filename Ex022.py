nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maísculo é {nome.upper()}. E seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem {nome.__len__() - nome.count(" ")} letras')
primeiro_nome = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro_nome} letras')