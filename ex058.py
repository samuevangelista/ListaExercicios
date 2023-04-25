from random import randint
from time import sleep
import os
n=randint(0,5)#numero computador
num = 7
c = 0
while num != n:
    print('Tente adivinhar o número do computador')
    num = int(input('Escolha um numero entre 0 e 5: '))
    print('PROCESSANDO...')
    sleep(1)
    if num == n:
        print('ACERTOU!')
    else:
        print('ERROU!\nTente novamente')
        sleep(2)
        os.system("cls")
    c +=1
print('Você precisou de {} tentativas para acertar'.format(c))