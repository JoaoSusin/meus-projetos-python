numeros = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desesete','desoito', 'desenove', 'vinte')
n = -1
while n not in range (0,21):
    n = int(input('Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {numeros[n-1]}') # numeros é a tupla e n é a posição. Logo o numero 10 mostra a posição 10 da tupla que é o dez