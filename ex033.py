def notas(*num, sit=False):
    tudo= {}
    tudo['Notastotal'] = len(num)
    tudo['MaiorNota'] = max(num)
    tudo['MenorNota'] = min(num)
    tudo['Media'] = sum(num) / len(num) #sum é a soma dos itens 
    if sit == True:
        if tudo['Media'] > 8:
            tudo['Situação'] = 'Muito beem!'
        elif tudo['Media'] >= 6: 
            tudo['Situação'] = 'Razoavel'
        else:
            print('Muito Ruim!')
    return tudo 
        
    
    
resp = notas(5.5, 2.5, 10, 8,)
print(resp)
