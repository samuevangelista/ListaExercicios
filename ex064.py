flag = 0
c = 0
s = 0
while flag != 999:
    flag = int(input("digite um numero: "))
    if flag != 999:
        s = s + flag
        c += 1
print('Você digitou {} numeros,a soma entre eles é {}'.format(c, s))