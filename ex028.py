import random
lista = []
def analisar(valor):
    print(f' Os valores sorteados foram {lista}')

def soma(valor):
    print(f'A soma dos numeros pares é {par}')










for n in range(5):
   numero = random.randint(1,10)
   lista.append(numero)
   
analisar(numero)

par = 0
if numero % 2 == 0:
    par = par + numero

soma(par)