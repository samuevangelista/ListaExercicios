import os
c = 0
num1 = int(input('Digite o 1° numero: '))
num2 = int(input('Digite o 2° numero: '))

while c != 5:
    c = int(input('[ 1 ] Somar\n'
               '[ 2 ] Multiplicar\n'
               '[ 3 ] Maior\n'
               '[ 4 ] Novos Numeros\n'
               '[ 5 ] Sair do programa\n'
               'Escolha: '))
    if c == 1:
        print('{} + {} = {} '.format(num1, num2, (num1 + num2)))
    elif c == 2:
        print('{} X {} = {} '.format(num1, num2, (num1 * num2)))
    elif c == 3:
        if num1 > num2:
            print('O numero {} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('O numero {} é maior que {}'.format(num2, num1))
        else:
            print('Os numeros são iguais')
    elif c == 4:
        print('Informe os numeros novamente')
        num1 = int(input('Digite o 1° numero: '))
        num2 = int(input('Digite o 2° numero: '))
        os.system("cls")
    elif c == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-=' * 10)
print('Programa Encerrado')