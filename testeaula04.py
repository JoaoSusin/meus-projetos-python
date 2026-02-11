#def contador (*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


#contador(2, 4, 5, 6)
#contador(6, 3, 6, 9)

def dobra(lst):
    pos = 0
    while pos <len(lst): # enquanto a pos for menor que o numero de elementos na lista, a minha lista na pos em que estiver, seja 0,1,2 ele vai multiplicar o valor por 2
       lst[pos]*=2
    pos +=1 # como a pos começa em 0, 0 é o primeiro item da lista, depois com o pos+=1 ele vai aumento 1 para multiplicar todos os numeros que estão na lista 
        


valores = [7, 2, 6, 8]
dobra(valores)
print(valores)

def soma(* valores):# O asterisco faz com que eu possa adicionar varios valores a lista
    s = 0 # minha resposta finla começa recebendo 0
    for num in valores:# para cada numero na variavel valores
        s += num # ele vai pegar a minha resposta final que é 0 e vai somar com o meu num que vai passar por todos os numeros que estão na variavel valor
        #ou seja se tem 7 numeros ele vai passar pelos 7 numeros somando cada um deles 
    print(f'A soma dos numeros {valores} é igual a {s}')
    

soma(3,7,9)
soma(2,43,21)