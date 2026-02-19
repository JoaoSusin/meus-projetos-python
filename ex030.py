def fatorial(numero, show):
    fat = 1
    for number in range(numero, 0 , -1):
        fat = fat * number
        if show:
            print(number, end='')
            if number >1:
                print(f' x ',end=' ')
            else:
                print(' = ',end='')
             
    return fat 
    
    
    
    
print(fatorial(5, show=False))# show false mostra so o resultado final e show true mostra toda a conta 

