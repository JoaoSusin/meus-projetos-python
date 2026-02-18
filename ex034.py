def ajuda():
    print('\033[31mFunção de Ajuda pyHelp\033[m')
    while True:
        palavra = (input('Função ou Biblioteca?[^ fim ^ para sair]:  '))
        if palavra.lower() == 'fim':
            print('Até logo')
            break
        
        help(eval(palavra))

ajuda()
        
      




