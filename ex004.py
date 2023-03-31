msg = 'DISECANDO A VARIÁVEL'
print('{:=^35}'.format(msg))
a = input('Digite algo:')
print('O tipo primitivo dessa variavel é ', type(a))
print('Só tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maiúsculo?', a.isupper())
print('Está em minusculo?', a.islower())
print('Está captalizada?', a.istitle())

