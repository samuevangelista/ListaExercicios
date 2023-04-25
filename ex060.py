n = int(input('Digite um numero: '))
c = n
f = 1
while c != 0:
    f = f * c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))