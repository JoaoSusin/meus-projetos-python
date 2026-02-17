def ficha(name='<desconhecido>' ,gol= 0 ):
    print(f'O jogador {name} fez {gol} gols no campeonato ')
    

nome = str(input('Qual o nome do jogador? '))
gols = str(input('Quantos gols o jogador marcou? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols= 0
    
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome,gols)
