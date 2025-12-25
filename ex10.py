numeros = []
r = 'S'
contador = 0 

while r == 'S':
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    contador += 1
    r = str(input('Quer continuar? [S/N]: ')).upper()
    numeros.sort(reverse=True)
if r == 'N':
    print(f'Foram digitados {contador} numeros.')   
    print(f'Os valores digitados em ordem decrescente ficaram assim: {numeros}')
    if 5  in numeros:
        print(f'O numero 5 aparece nessa lista')
    else:
        print('O numero 5 não aparece nessa lista')