def leiaint(msg):
    while True:
        numero = input(msg)
        if  numero.isnumeric():#esse is numeric ele pega uma str e vese é um numero
            return int(numero)# se for o return int(numero), retorna o valor intiro da str 
    
        else:
            print('ERRO, Digite um numero válido! ')





n = leiaint('Digite um numero ')
print(f'Você acabou de digitar o numero {n}')