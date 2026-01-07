jogador = {}
partidas = ()
gols = []


jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou:  '))
for part in range(0, partidas):
    gol = int(input(f'Quanto gols na partida {part}? '))
    gols.append(gol)
    jogador['gols'] = gols
    
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)
for partida, golo in enumerate(jogador['gols']):
    print(f' => na partida {partida} fez {golo} gols')
