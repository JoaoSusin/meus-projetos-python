#galera = [['Joao', 12], ['Maria', 19], ['Antonia', 15]]
#for p in galera:
 #   print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # aqui ele limpa oque foi colocado em dado pra nao aparecer repetido na hora de executar, e mostra so uma vez no galera
print(galera)

for p in galera:
    if p[1] > 21:
        print (f'{p[0 ]} é maior de idade ')
    else:
        print(f'{p[0]} é menor de idade')