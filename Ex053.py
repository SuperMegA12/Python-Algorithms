frase = str(input('Digite uma frase para saber seu inverso: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso+=junto[letras]
if inverso == junto:
     print(f'A frase {frase} é palíndromo')
else:
   print(f'A frase {frase} não é palíndromo')



#Ex053 - Detector de Palíndromo