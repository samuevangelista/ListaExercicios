from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
tupla  = (n1, n2, n3, n4, n5)
print('Os valores sortados foram: ', end='')
maior = menor = 0
for pos, c in enumerate(tupla):
    print(f'{c}', end= ' ')
    if pos == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')