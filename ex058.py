from random import randint
n=randint(0,5)#numero computador
print('Tente adivinhar o número do computador')
print('Escolha um numero entre 0 e 5! ')
c = 0
acertou = False
while not acertou:
    num = int(input('Palpite: '))
    c += 1
    if num == n:
        print('ACERTOU!')
        acertou = True
    else:
        if num < n:
            print('Mais... Tente novamente')
        elif num > n:
            print('Menos... Tent novamente')

print('Você precisou de {} tentativas para acertar'.format(c))