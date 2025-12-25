matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = maior = scoluna = 0

for l in range(0,3):
    for c in range (0,3):
        matriz[l] [c] = int(input(f'Diga um valor {l},{c}: ')) 
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^5}]', end=' ')
    print()
    if matriz[l][c] % 2 == 0:
        spar += matriz[l][c]
for l in range(0,3):
    scoluna += matriz[l][2]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos pares são {spar}')
print(f'A soma dos valores da terceira coluna é {scoluna}')
print(f'O maior numero da segunda linha é {maior}')

