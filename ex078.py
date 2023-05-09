tupla = []
menor = maior = 0
for c in range(1,6):
    n = int(input(f'Digite um valor para a Posição {c}: '))
    tupla.append(n)
    if c == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Você digitou os valores {tupla}')
print(f'O maior valor digitado foi {maior} nas posição ', end = '')
for pos, c in enumerate(tupla):
    if c == maior:
        print(f'{pos + 1}...', end = '')
print(f'\nO menor valor digitado foi {menor} nas posição ', end = '')
for pos, c in enumerate(tupla):
    if c == menor:
        print(f'{pos + 1}...', end = '')
