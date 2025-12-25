dados = list()
cadastrados= list()
r = 'S'
contador = 0
while r == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    cadastrados.append(dados[:])
    dados.clear()
    contador += 1
print(f'o total de pessoas cadastradas foram {contador}')
print(f'As pessoas cadastradas foram: {cadastrados}')

for p in cadastrados:
    if p[1] >= 70:
        print(F'{p[0]} pesa {p[1]} e está acima do peso')
    else:
        print(f'{p[0]} pesa {p[1]} e não está acima do peso')
