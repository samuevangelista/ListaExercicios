sexo=''
while True:
    print('-'*20)
    print('CADATRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
