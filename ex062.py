i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
d = 0
m = 1
'''
u = i + (10-1) * r
for c in range(i, u + r, r):
    print('{}'.format(c), end='-> ')
print('ACABOU')'''
while c < 10:
    print('{}'.format(i), end='-> ')
    i = i + r
    c += 1
print(' \n')
while m != 0:
    m = int(input('Você quer mais quantos termos?: '))
    while d < m:
        print('{}'.format(i), end='-> ')
        i = i + r
        c += 1
    print(' \n')
print('ACABOU, {} termos'.format(c))