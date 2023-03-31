n = int(input('Digite um numero: '))
cont = 1
while cont <= 10:
    mult = n * cont
    print('{} x {:2} = {}'.format(n, cont, mult))
    cont += 1