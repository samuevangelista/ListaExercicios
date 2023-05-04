from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0
while True:
    print('=-' * 15)
    comp = randint(0, 5)  # numero computador
    valor = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    resto = (valor + comp) % 2
    if resto == 1:
        resultado = 'I'
        print(f'Você jogou {valor} e o computador {comp}. '
              f'Total de {(valor + comp)} DEU ÍMPAR')
    if resto == 0:
        resultado = 'P'
        print(f'Você jogou {valor} e o computador {comp}. '
              f'Total de {(valor + comp)} DEU PAR')
    print('-'*30)
    if resultado == escolha:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        break
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')