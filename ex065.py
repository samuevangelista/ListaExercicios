r = 'S'
maior = 0
menor = 0
c = 0
s = 0
while r != 'N':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    s += n
    if n > maior:
        maior = n
        menor = n
    elif n < menor:
        menor = n
    c += 1
print('A media dos valores digitados foi {}'.format((s / c)))
print('O maior numero foi {}, o menor numero foi {}'.format(maior, menor))