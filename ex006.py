palavras = ('aprender', 'python', 'curso', 'gratis', 'estudar', 'trabalhar')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos:' , end=' ' )
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal,end= '')