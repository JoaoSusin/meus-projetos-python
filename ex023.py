jogador = {}
partidas = ()
todos_jogadores = []
continuar = 'S'
total_goals = 0

while continuar == 'S':
    gols = []
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou:  '))
    for part in range(0, partidas):
        gol = int(input(f'Quanto gols na partida {part +1}? '))
        gols.append(gol)
        jogador['gols'] = gols
        jogador['Total'] = sum(gols)
    todos_jogadores.append(jogador.copy())
    
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N')

for jogador in todos_jogadores:
    print(f'O jogador {jogador["Nome"]} tem um total de {jogador["Total"]}')

print('-'*30)
 
print('-' * 50)
print(f'{"Pos":<4}{"Nome":<15}{"Gols":<15}{"Total":<7}')
print('-' * 50)

for pos, jogador in enumerate(todos_jogadores):
    print(f'{pos:<4}{jogador["Nome"]:<15}{str(jogador["gols"]):<15}{jogador["Total"]:<7}')
