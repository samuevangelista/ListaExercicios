from random import randint
n = randint(0,9999)
#n = input('Digite um numero entre 0 e 9999: ' )
print('Numero aleatorio foi {}'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {} '.format(d))
print('centena: {} '.format(c))
print('milhar: {}'.format(m))







