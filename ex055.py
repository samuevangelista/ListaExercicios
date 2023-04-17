maior = 0
for c in range(1, 6):
    peso = int(input('Pesos: '))
    if peso > maior:
        maior = peso
        menor = peso
    elif peso < menor:
        menor = peso
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))