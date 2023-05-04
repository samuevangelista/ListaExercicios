maioridade = homens = menosvinte = 0
while True:
    sexo = continuar = ' '
    print('-'*20)
    print('CADATRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        menosvinte += 1

    if continuar == 'N':
        break
print('FIM PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {menosvinte} mulheres com menos de 20 anos')