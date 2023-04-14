from random import randint
from time import sleep
n = randint(1,3)
print('=== JOKENPÔ ===')
nn = int(input('-VAMOS JOGAR-\n'
                    '[1] |PEDRA|   \n'
                    '[2] |PAPEL|   \n'
                    '[3] |TESOURA| \n'
                    '(Escolha): '))
print('==============\n '
      'PROCESSANDO...\n'
      '==============')
sleep(3)
if n == nn:
    if n == 1:
        emp = 'PEDRA'
    elif n == 2:
        emp = 'PAPEL'
    else:
        emp = 'TESOURA'
    print('{} X {}'.format(emp, emp))
    print('EMPATE')
else:
    if n == 1 and nn == 2:
        print('PEDRA X PAPEL')
        print('VOCE GANHOU')
    elif n == 1 and nn == 3:
        print('PEDRA X TESOURA')
        print('VOCE PERDEU')
    elif n == 2 and nn == 1:
        print('PAPEL X PEDRA')
        print('VOCE PERDEU')
    elif n == 2 and nn == 3:
        print('PAPEL X TESOURA')
        print('VOCE GANHOU')
    elif n == 3 and nn == 1:
        print('TESOURA X PEDRA')
        print('VOCE GANHOU')
    elif n == 3 and nn == 2:
        print('TESOURA X PAPEL')
        print('VOCE PERDEU')