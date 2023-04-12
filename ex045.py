from random import randint
from time import sleep
n = randint(1,3)
print('=== JOKENPÔ ===')
escolha = int(input('-VAMOS JOGAR-\n'
                    '|PEDRA|   [1]\n'
                    '|PAPEL|   [2]\n'
                    '|TESOURA| [3]\n'
                    '(Escolha): '))
print('PROCESSANDO...')
sleep(3)
if n == 1 and escolha == 1:
    