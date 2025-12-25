from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos você deseja fazer? '))
tot = 1
while tot <= quant:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os numeros sorteados foram {jogos}')
