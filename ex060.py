n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando {}!: '.format(n), end='')
while c != 0:
    f = f * c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))