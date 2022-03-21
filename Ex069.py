cont_idade = cont_man = cont_woman =  0
while True:
    idade = int(input('Digite sua idade: '))
    if idade >18:
        cont_idade+=1
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        cont_man+=1
    if idade < 20 and sexo == 'F':
        cont_woman+=1
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua == 'N':
        break
print(f'Ha {cont_idade} pessoa(s) maior(es) que 18 anos registrados.')
print(f' Ha {cont_man} homens registrados.')
print(f'Ha {cont_woman} mulheres com menos de 20 anos.')