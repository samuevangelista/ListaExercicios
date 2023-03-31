import math

print('{:=^40}'.format('CAUCULA TRIANGULO'))
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
'''h = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))'''
h = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(h))

