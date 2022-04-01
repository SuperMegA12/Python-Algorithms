abreParent = []

expressao = input('Digite uma expressão: ').strip().lower()

for caracter in expressao:
    if caracter == '(':
        abreParent.append(caracter)

    if caracter == ')':
        abreParent.pop() if len(abreParent) > 0 else abreParent.append(')')

print('Expressão Correta...' if len(abreParent) == 0 else 'Expressão incorreta...')



#Ex083 - Validando Expressões Matemáticas