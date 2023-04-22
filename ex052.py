n = int(input("Digite um numero: "))
mult=0
for c in range(1,n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print("\n\033[m0 Tem {} múltiplos acima de 2 e abaixo de {}".format(mult, n))

if(mult==2):
    print("É primo")
else:
    print("Não é primo")
