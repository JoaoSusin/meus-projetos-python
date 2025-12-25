num = [2,5,9,1]
num[2] = 3
num.append(4)
num.sort(reverse=True)
num.insert(2, 2)
if 6 in num:
    num.remove(6)
else:
    print('Nao achei nenhum numero 6')
print(num)
print(f'Essa lista tem {len(num)} elementos')