"""i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(i,  , r):
    print(c)"""
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
u = i + (10-1)*r
for c in range(i, u + 1, r):
    print(c)