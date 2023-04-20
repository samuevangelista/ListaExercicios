s = 0
con = 0
for c in range(1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        con += 1
print('Você informou {} numeros pares, a soma é {}'.format(con, s))