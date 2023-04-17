print('Soma de todos os números ímpares multiplos de 3')
s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
print(s)