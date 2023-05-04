extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numero = 11
while numero < 0 or numero > 10:
    numero = int(input('Digite um numero entre 0 e 10: '))
print(f'Você digitou o número {extenso[numero]}')