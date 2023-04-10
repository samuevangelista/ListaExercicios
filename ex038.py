n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('O \033[0;33m primeiro valor\033[m é \033[0;34m maior\033[m')
elif n2 > n1:
    print('O \033[0;33m segundo valor\033[m é \033[0;34m maior\033[m')
else:
    print('\033[0;33m Não existe\033[m valor maior, os dois são \033[0;34m iguais\033[m')