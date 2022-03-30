array = []
while True:
    values = int(input('Enter a value: '))
    while values in array:
        print('Duplicated value. It has not been added')
        values = int(input('Enter a value: '))
    else:
        array.append(values)
    question = str(input('Do you want to keep adding values? [Y/N]: ')).strip().upper()
    if question != 'Y':
        break


array.sort()
print(f'Entered Values: {array}')

#Ex079 - Valores únicos em uma lista