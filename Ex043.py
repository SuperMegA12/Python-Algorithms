altura = float(input('Digite a sua altura: CM'))
peso = float(input('Digite o seu peso: KG'))
imc = peso / (altura**2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc <= 25:
    print('Você está no seu peso ideal.')
elif 25 < imc <= 30:
    print('Você está com sobrepeso')
elif 30 < imc <= 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('ALERTA!! OBESIDADE MORBIDA!')