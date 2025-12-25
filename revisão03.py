a = [0,2,3,5]
b = a[:]# isso siginifica que ele vai pegar todos os valores de A e jogar em B( nao cria ligação, cria uma cópia)
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')