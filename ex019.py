aluno = {}
escola = []

aluno['Nome'] = str(input('Qual o nome do aluno: '))
aluno['Media'] = int(input('Qual a media do aluno: '))
escola.append(aluno.copy())

print(f'O nome do aluno é {aluno["Nome"]}')
print(f'A media do aluno é {aluno["Media"]}')
if aluno['Media'] >= 7:
    print(f'O aluno {aluno["Nome"]} passou de ano ')
else:
    print('O aluno Reprovou de ano')

