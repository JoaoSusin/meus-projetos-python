def maior (* num ):
    contador = 0
    nummaior = 0
    for n in num:
        contador = contador + 1 
        if n > nummaior:
            nummaior = n    
    print(f'Essa lista tem um total de {contador} numeros {num}')
    print(f'O maior numero dessa lista é {nummaior}')
    
    
    
    
maior(6,7,3,10,8)
maior(0,8,7)
maior(3,6,2)