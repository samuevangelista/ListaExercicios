from random import randint
n=randint(0,5)#numero computador
print('Tente adivinhar o número do computador')
num = int(input('Escolha um numero entre 0 e 5: '))
if num == n:
    print('ACERTOU!')
else:
    print('ERROU!')
    print('O certo seria {}'.format(n))

#print('ACERTOU!' if npc == n else 'ERROU!')
