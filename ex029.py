from datetime import date
ano_atual = date.today().year
def voto(nasc):
    idade = ano_atual - nasc
    if idade >= 18 and idade < 65:
        print(f'o usuário tem {idade} e deve votar ')
    elif idade < 18:
        print(F'O usuario tem {idade} e não pode votar')
    elif idade >= 65:
        print(f'O usuario tem mais de 65 anos e não é obrigado a votar')


nasc = int(input('Qual o ano de nascimento? '))
voto(nasc)