n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print('O {} é o MAIOR numero'.format(n1))
elif n2 > n3:
    print('O {} é o MAIOR numero'.format(n2))
else:
    print('O {} é o MAIOR numero'.format(n3))

if n1 < n2 and n1 < n3:
    print('O {} é o MENOR numero'.format(n1))
elif n2 < n3:
    print('O {} é o MENOR numero'.format(n2))
else:
    print('O {} é o MENOR numero'.format(n3))
