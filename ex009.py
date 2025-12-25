numero = []
for n in range( 0,5):
     valor = (int(input('Digite um numero: ')))
     if n == 0:
        numero.append(valor)
        print(f'O numero {valor} foi adicionado na primeira posição')
     elif valor > numero [-1]:
         numero.append(valor)
         print(f'O numero {valor} foi adicionado na ultima posição da lista ')
     else:
        pos = 0
        while pos < len(numero):
            if valor <= numero[pos]:
                numero.insert(pos, valor)
                print(f'O numero {valor} foi adiconado na posição {pos}')
                break
            pos += 1

print(f'os numeros digitados em ordem foram {numero}')
    
                
    
      
        
        
    