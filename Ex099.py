from time import sleep

def maior(*n):
    print('=-' * 30)
    print('Analisando os valores passados...')
    if len(n) > 0:
        for i in n:
            print(f'{i} ', end='')
            sleep(0.5)
        print(f'O maior valor informado foi {max(n)}')
    else:
        print('A função não recebeu valores')



maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)


#Ex99 - Função que descobre o maior
