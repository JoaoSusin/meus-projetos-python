dados = []
alunos = []
R = 'S'
while R == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    alunos.append(dados[:])
    dados.clear()
    R =str(input('Quer continuar? [S/N] ')).strip().upper()
print (alunos)
for aluno in alunos:
    media = (aluno[1] + aluno[2]) /2

    if media >= 6:
        print(f'o aluno {aluno[0]} foi aprovado com media {media:.1f}')
    else:
        print(f'o aluno {aluno[0]} foi reprovado com media {media:.1f}')
       
        

print(dados)