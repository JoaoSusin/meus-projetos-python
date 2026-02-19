#modularização serve para dividir um programa grande em pequenos pedaçoes
#=> fazer um novo file para colocar as funçoes e deixar o programa principal so em uma pag
from uteis.numeros import numeros
num = int(input('Digite um valor: '))
fat=numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')