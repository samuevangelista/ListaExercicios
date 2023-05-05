n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o último numero: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 pareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {(tupla.index(3) + 1)}° posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
par = 0
print(f'Os valores pares digitados foram', end =' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')
