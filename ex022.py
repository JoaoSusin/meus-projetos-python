continuar = 'S'
cadastradas = 0
mulheres = []
soma_idade = 0
pessoas = []
acima_da_media = []
media_idade = 0


while continuar == 'S':
    pessoa = {}

    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    soma_idade += pessoa['Idade']
    cadastradas += 1
    

# validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoas.append(pessoa)    
# validação do continuar
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N')
media_idade = soma_idade/cadastradas
for p in pessoas:
    if p['Idade'] > media_idade:
        acima_da_media.append(p['Nome'])

print(f'Foram cadastradas {cadastradas} pessoas')
if mulheres:
    print('Foram cadastradas as mulheres:', ', '.join(mulheres))
else:
    print('Nenhuma mulher foi cadastrada')
print(f'A média de idade é {media_idade:.1f} anos')
if acima_da_media:
    print('Pessoas acima da média:', ', '.join(acima_da_media))
else:
    print('Ninguém está acima da média')






