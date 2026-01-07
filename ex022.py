continuar = 'S'

while continuar == 'S':
    pessoa = {}

    pessoa['Nome'] = str(input('Nome: '))

    # validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')

    # validação do continuar
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N')

print('Programa encerrado.')


