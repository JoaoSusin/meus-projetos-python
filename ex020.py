pessoa = {}
geral = []
pessoa['Nome'] = str(input('Qual o seu nome: '))
pessoa['idade'] = int(input('Qual a sua idade: '))
pessoa['carteira'] = int(input('Digite o numero da sua carteira de trabalho, (digite zero de não tiver): '))
geral.append(pessoa.copy())

if pessoa['carteira'] == 0:
     print(f" - Pessoa tem o valor {pessoa["Nome"]}\n - Idade tem o valor {pessoa["idade"]}\n - Carteira tem o valor {pessoa["carteira"]}")
else:
     pessoa['ano'] = int(input('Qual o ano de contratação:  '))
     pessoa['salario'] = int(input('Qual o seu salário R$: '))
     print(f" - Pessoa tem o valor {pessoa["Nome"]}\n - Idade tem o valor {pessoa["idade"]}\n - Carteira tem o valor {pessoa["carteira"]}\n - A pessoa foi contratada no ano de {pessoa["ano"]}\n - O salario dessa pessoa é {pessoa["salario"]} R$")

    
      
          

