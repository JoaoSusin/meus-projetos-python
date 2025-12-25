comidas = ['refri', 'hamburger', 'cachorro quente', 'cookie']
print(comidas)
comidas.append('coca')#para adicionar itens na lista
print(comidas)
comidas.insert(0,'cafe')#para adicionar cafe na posição zero
del comidas[3]# deleta o item 3 de comidas 
valores = list(range(4,11))#cria uma lista de 4 a 10 
valores = [5,2,6,7,4,2]# cria uma lista com esses numeros, e para ficar em ordem é so usar o valores.sort(), e pra criar em ordem reversa e só usar o valores.sort(reverse=True)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}') # o enumerate faz com que eu consiga dizer em que posição está o valor
valores.append(int(input('Digite um valor: ')))