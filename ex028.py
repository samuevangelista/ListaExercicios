from random import randint
from time import sleep
n=randint(0,5)#numero computador
print('Tente adivinhar o número do computador')
num = int(input('Escolha um numero entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if num == n:
    print('ACERTOU!')
else:
    print('ERROU!')
    print('O certo seria {}'.format(n))
