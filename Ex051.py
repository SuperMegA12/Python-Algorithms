primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao_pa = int(input('Digite a razão da PA:'))
termos_usuario = int(input('Quantos termos você quer saber? :'))
termos_calcular = primeiro_termo + (termos_usuario - 1) * razao_pa
for c in range(primeiro_termo, termos_calcular + razao_pa, razao_pa):
    print(c)



#Ex051 - Progressão Aritimética
