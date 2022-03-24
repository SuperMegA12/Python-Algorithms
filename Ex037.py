
n = int(input('Digite um número inteiro: '))
escolha = int(input('Digite [1] para converter em binário.'
                    ' Digite [2] para converter em octal.'
                    ' Digite [3] para converter em hexadecimal: '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)
if escolha == 1:
    print(f'O número {n} em binário é {binario}')
elif escolha == 2:
    print(f'O número {n} em octal é {octal} ')
elif escolha == 3:
    print(f'O número {n} em hexadecimal é {hexadecimal}')
else:
    print(f'Opção {escolha} não está na lista. Digite um número válido.')



#Ex037 - Conversor de Bases Numéricas