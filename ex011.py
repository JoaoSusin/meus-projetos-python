numeros = []
r = 'S'
impar = []
par = []
while r == 'S':
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'A lista completa de numeros é {numeros}')
print(f'A lista de numeros pares é {par}')
print(f'A lista de numeros impares é {impar}')