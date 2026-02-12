from  random import randint
def sortear(lista):
    for cont in range(0,5):
        cont = randint(0,10)
        numeros.append(cont)

def somapar(numpar):
    par = 0
    for n in numeros:
        if n % 2 == 0:
            par += n
    print(par)        

    
    


numeros = []
sortear(numeros)
print(numeros)
somapar(numeros)
