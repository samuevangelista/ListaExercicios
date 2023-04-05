ano = int(input('Digite um ano qualquer: '))
r = ano % 4
if r == 0:
    print('O ano inserido é bisexto')
else:
    print('O ano é normal')