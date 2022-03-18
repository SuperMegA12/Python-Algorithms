primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao_pa = int(input('Digite a razão da PA:'))
termos_usuario = int(input('Quantos termos você quer saber? :'))
termo = primeiro_termo
cont = 1
while cont <= termos_usuario:
    print(f'{termo}')
    termo+=razao_pa
    cont+=1