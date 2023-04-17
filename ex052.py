"""n = int(input('Digite um numero: '))
if n % 1 == n and """
n = int(input("Digite um numero: "))
mult=0

for c in range(2,n):
    if (n % c == 0):
        print("Múltiplo de",c)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
