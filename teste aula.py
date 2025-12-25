teste = list()
teste.append('Marcelo')
teste.append(23)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera)