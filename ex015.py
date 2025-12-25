matriz = [[0,0,0],[0,0,0],[0,0,0]]


for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor {l}, {c}: '))
#print(f'  {matriz[0]}\n {matriz[1]}\n {matriz[2]}') pode ser feito assim tambem, mas vou fazer como ta na aula
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()