n1 = float(input('Digite da 1º reta: '))
n2 = float(input('Digite da 2º reta: '))
n3 = float(input('Digite da 3º reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('è possivel criar um triangulo')
else:
    print('N è possivel criar um triangulo')