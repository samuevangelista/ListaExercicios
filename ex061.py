i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
'''
u = i + (10-1) * r
for c in range(i, u + r, r):
    print('{}'.format(c), end='-> ')
print('ACABOU')'''
while c <= 10:
    print('{}'.format(i), end='-> ')
    i += r
    c += 1
print('ACABOU')