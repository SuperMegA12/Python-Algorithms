nome = str(input('Digite um nome: ')).upper().strip()
cont = 0
if ('A' in nome):
    caio = nome.count('A')
    achar = nome.find('A')
    encontrar = nome.rfind('A')
    print(f'Seu nome possui a letra "\A"\. Ela aparece {caio} vezes, na posição {achar} pela primeira vez no seu nome.'
     f' E na posição {encontrar} pela última vez.')
