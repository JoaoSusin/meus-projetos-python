#pessoas = {'nome':'Gustavo', 'sexo': 'Masculino', 'idade': 20}
#pessoas['peso'] = 98.5
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#for k ,v in pessoas.items():
#   print(f'{k} = {v}')

#brasil = []
#estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]['uf'])

estado = {}
brasil = []
for c in range (0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)