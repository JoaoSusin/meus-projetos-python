def leiaint(msg):
    while True:
        numero = input(msg)
        if  numero.isnumeric():
            return int(numero)
    
        else:
            print('ERRO, Digite um numero válido! ')





n = leiaint('Digite um numero ')
print(f'Você acabou de digitar o numero {n}')