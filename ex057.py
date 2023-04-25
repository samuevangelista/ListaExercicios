sexo = 'J'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o seu sexo?[M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido\nTente novamente')
print('sexo Valido')