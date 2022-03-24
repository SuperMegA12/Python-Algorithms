from random import randint
number = randint(0,5)
guess = int(input('Entre 0 e 5, qual número eu pensei? : '))
while guess > 5 or guess < 0:
    guess = int(input('Alternativa inválida, digite novamente.Entre 0 e 5, qual número eu pensei? : '))
if guess == number:
    print(f'Parabéns! Eu realmente pensei no número {number}')
else:
    print(f'Você errou!Eu pensei no número {number}')




#Ex028 - Jogo da Advinhação
