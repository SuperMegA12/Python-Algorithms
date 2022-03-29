tupla = ('MERCADO', 'PROGRAMADOR', 'HERCULES', 'GUANABARA','PYTHON')
vogais =  ('A', 'E','I','O','U')
for i in tupla:
    print('=-'*10)
    print(f'A palavra {i} tem as vogais: ')
    for letras in i:
        for vogal in vogais:
            if vogal == letras:
                print(f'{vogal}')




#Ex077 - Contando vogais em tuplas
