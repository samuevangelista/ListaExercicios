from random import randint
tupla  = (randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10))
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