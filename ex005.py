produtos = ('lápis ', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'mochila', 120)
for itens in range (0, len(produtos)):
    if itens % 2 ==0:
        print(f'{produtos[itens]:.<30},R$', end= '')
    else:
        print(f'{produtos[itens]:>5.2f}')

