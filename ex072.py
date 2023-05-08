extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    while True:
        numero = int(input('Digite um numero entre 0 e 10: '))
        if 0 <= numero <= 10:
            break
        print('Tente novamente.', end = '')
    print(f'Você digitou o número {extenso[numero]}')
    resp = 'J'
    while resp not in 'SN':
        resp = str(input(f'Você quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('Fim programa')