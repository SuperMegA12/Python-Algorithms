#O código antes da linha 8 é só para uma praticidade de adiconar os nomes.
tupla = ()
transformando = list(tupla)
for c in range(0,21):
    n = str(input(f'{c}ª: ')).strip().upper()
    transformando.append(n)
tupla = tuple(transformando)

######################################
while True:
   question = int(input('Qual número você quer saber sua forma extensa de 0 a 20? : '))
   if question > 20:
       question = int(input('Termo inválido. Qual número você quer saber sua forma extensa de 0 a 20? : '))
   elif question < 0:
       break
   print(f'Você digitou o número {tupla[question]}')


#Ex072 - Números por extenso



