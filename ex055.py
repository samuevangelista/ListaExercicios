maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Pesos: '))
    if peso > maior:
        maior = peso
        menor = peso
    elif peso < menor:
        menor = peso
print('Maior peso: {}Kg'.format(maior))
print('Menor peso: {}Kg'.format(menor))