
n = int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: '))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)}x') # para contar quantas vezes apareceu o numero 9
print(f'O primeiro numero 3 está na posição {n.index(3)} ')
for par in n:
    if par % 2 == 0:
        print(f'Os numeros pares são {par}')
        

