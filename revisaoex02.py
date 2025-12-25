numeros = []
r = 'S'
while  r == 'S':
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print(f'O numero {valor} ja foi digitado ')
    else:
        numeros.append(valor)
        print(f'O valor {valor} foi cadastrado com sucesso!')
    r = str(input('Deseja continuar? [S/N]: ')).upper()
numeros.sort()
print(f'A lista possui esses numeros {numeros}')
