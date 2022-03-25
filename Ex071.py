n = int(input('Digite o valor que deseja sacar: R$ '))
#Apenas inteiros
total = n
ced = 50
totalced = 0
while True:
   if total >= ced:
       total -= ced
       totalced +=1
   else:
       if totalced > 0:
         print(f'Total de {totalced} cédulas de {ced} R$')
       if ced == 50:
         ced = 20
       elif ced == 20:
        ced = 10
       elif ced == 10:
         ced = 1
       totalced = 0
       if total == 0 :
        break



#Ex071 - Simulador de Caixa Eletrônico
