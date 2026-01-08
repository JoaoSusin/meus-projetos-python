jogador = {}
partidas = ()
gols = []
todos_jogadores = []
continuar = 'S'

while continuar == 'S':
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou:  '))
    for part in range(0, partidas):
        gol = int(input(f'Quanto gols na partida {part}? '))
        gols.append(gol)
        jogador['gols'] = gols
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N')

    
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)
for partida, golo in enumerate(jogador['gols']):
    print(f' => na partida {partida} fez {golo} gols')