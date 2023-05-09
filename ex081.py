lista = []
cont = 0
while True:
    list.append(int(input('Digite um número: ')))
    cont += 1

    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
