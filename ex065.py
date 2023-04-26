r = 'S'
maior = menor = c = s = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = s / c
print('A media dos valores digitados foi {}'.format(media))
print('O maior numero foi {}, o menor numero foi {}'.format(maior, menor))