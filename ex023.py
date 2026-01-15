jogador = {}
partidas = ()
todos_jogadores = []
continuar = 'S'
total_goals = 0
resp = 0

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
#se a pessoa  digitar o numero de tal jogador, vou exibir os gols de tal jogador em cada partida 

while resp != 999:
    resp = int(input('Digite o codigo de qual jogador você deseja saber os dados (999 para sair):'))
    if resp == 999:
        print('saindo...')
        break
    elif resp < 0 or resp >= len(todos_jogadores):
        print('Codigo inválido')
    else:
        jogador = todos_jogadores[resp]# isso pega o jogador que esta na ´posição da resposta e joga todos os dados dele pra dentro de jogador
        print(f'Levantamento do jogador {jogador["Nome"]}:')
        
        for part , gols in enumerate(jogador["gols"]):
            print(f'Na partida {part +1} o jogador fez {gols} gols')
