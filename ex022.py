
nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ", ""))))
d = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(d[0])))