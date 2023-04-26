i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
'''c = 0
m = 1
while c < 10:
    print('{}'.format(i), end='-> ')
    i = i + r
    c += 1
print(' \n')
c = 0
while m != 0:
    m = int(input('Você quer mais quantos termos?: '))

    while c < m:
        print('{}'.format(i), end='-> ')
        i = i + r
        c += 1
    print(' \n')
print('ACABOU')'''
termo = i
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} > '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostras a mais? '))
print('FIM, {} termos mostrados'.format(c))