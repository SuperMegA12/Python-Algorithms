from random import randint




def sorteia(*n):
   print('Os 5 números sorteados foram: ', end='')
   soma = 0
   for i in n:
       print(f'{i} ', end='')
       if i % 2 == 0:
           soma+=i
   print(f'\nSomando os valores pares, o resultado é: {soma}')




sorteia(randint(0,10), randint(0,10), randint(0,10),randint(0,10),randint(0,10))



#Ex100 - Função para sortear e somar
