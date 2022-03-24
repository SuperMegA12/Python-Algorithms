primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razãp da PA: '))
mais = int(input('Quantos termos gostaria de saber? : '))
termos = primeiro
cont = 1
total = 0
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termos}')
        termos += razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos gostaria de saber a mais? : '))
print('FIM')



#Ex062 - Super Progressão Aritimética v3.0