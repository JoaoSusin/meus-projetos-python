valores = []
for v in range(0,5):
    valores.append(int(input(f'Digite {v+1}o valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}')
print(f'O menor valor digitado foi {min(valores)}')
