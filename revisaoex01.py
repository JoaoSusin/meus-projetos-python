num = []
for n in range(0,5):
    num.append(int(input('Digite um valor: ')))
for c, n in enumerate(num):
    print(f'Na posição {c} se encontra o valor {n}')

print(f'O maior valor digitado foi {max(num)}')
print(f'O menor valor digitado foi {min(num)}')