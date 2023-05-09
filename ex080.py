lista = []
maior = 0
for c in range(0,5):
    n = int(input('Digite um valor: '))
    lista.append(n)
    lista.sort()
    if n > maior:
        maior = n
        print('Adicionado ao final da lista...')
    else:
        print(f'adicionado na posição {lista.index(n)} da lista...')
print(f'Os valores digitados foram {lista}')