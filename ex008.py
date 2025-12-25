numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else: 
        print('O numero que você digitou já esta na lista!')
    
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Os valores digitados foram {numeros}')