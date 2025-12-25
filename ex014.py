numeros = [[], []]
valor = 0


for numero in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares dessa lista são {numeros[0]}')
print(f'Os numeros impares dessa lista são {numeros[1]}')


