flag = c = s = 0
while flag != 999:
    flag = int(input("digite um numero [999 para parar]: "))
    if flag != 999:
        s = s + flag
        c += 1
print('Você digitou {} numeros,a soma entre eles foi {}'.format(c, s))