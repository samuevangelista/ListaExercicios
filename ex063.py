n = int(input('Digite um numero: '))
c = 0
p = 1
s = 1
t  = 0
while c < n:
    t = p + s
    print('{}'.format(t), end='-> ')
    s = p
    p = t
    c += 1