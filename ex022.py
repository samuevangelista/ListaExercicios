msg = 'PROGRMA Texto'
print('{:=^35}'.format(msg))
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
dividido = nome.split()
print(len(dividido[0]))