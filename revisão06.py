#def teste(b):
    #global a # o valor  de A no escopo global vai valer 8 tambem, isso que o global modifica
    #a = 8
    #b += 4
    #c= 2
    #print(f'o valor de a é {a}')
    #print(f'o valor de b é {b}')
    #print(f'o valor de c é {c}')
    
    
    
#a = 2
#teste(a)
#print(f'O valor de a no escopo global é {a}')
##########################################
def somar(a,b,c):
    s = a+b+c
    return s


r1 = somar(3,4,6)
r2 = somar (2,6,1)
r3 = somar(9,0,3)
print(f'A soma vale  de todos os numeros é {r1, r2, r3}')