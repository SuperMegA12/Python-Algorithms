n1 = float(input('Digite a 1ª nota:'))
n2 = float(input('Digite a 2ª nota:'))
media = (n1 + n2) / 2
if media >=7:
    print(f'Sua média é de {media:.1f} Você foi aprovado!!')
elif media >= 5 and media <=6.9:
    print(f'Sua média é de {media:.1f} Você está em recuperação.')
elif media <5:
    print(f'Sua média é {media:.1f} Você foi reprovado!')