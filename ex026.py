import time 
def contador(inicio,fim,passo):
    
    if passo == 0:  
        passo = 1 # isso pra loop nao ser infinito sem mudar de lugar 
    if inicio > fim and passo > 0: # se o meu inicio for maior que o meu final tipo i=8 e f= -6 e o meu passo for maior que 0, tipo 2
        passo = - passo # o meu passo vai receber o sinal de negativo quando diminuir de zero o valor
    for i in range(inicio, fim + passo, passo):# ele soma o fim mais o passo pra sempre mostrar o ultimo valor, se nao se eu digitar o fim 9 ele mostra so  ate o 8
        print(f'{i}, \n', end=' ',)# para cada numero no inicio meio e fim respeitando o passo, ele vai mostrar o numero
        time.sleep(0.5)# em um cooldown de 0.5 seg

print('Contagem de 0 até 10')
for i in range(0,11):
    print(f'{i}' , end=' ', )
    time.sleep(0.5)
    


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)