sexo = 'J'
while sexo not in 'MmFf':
    sexo = str(input('Qual é o seu sexo?[M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido, Tente novamente')
print('sexo Valido')