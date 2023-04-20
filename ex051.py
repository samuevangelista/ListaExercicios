"""i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(i,  , r):
    print(c)"""
i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
u = i + (10-1) * r
for c in range(i, u + r, r):
    print('{}'.format(c), end='-> ')
print('ACABOU')