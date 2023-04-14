n1 = float(input('Digite da 1º reta: '))
n2 = float(input('Digite da 2º reta: '))
n3 = float(input('Digite da 3º reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel criar um triangulo ')
    if n1 == n2 == n3:
        print('O trinagulo formado é o EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('O trinagulo formado é o ISÓSCELES')
    else:
        print('O trinagulo formado é o ESCALENO')
else:
    print('N è possivel criar um triangulo')

