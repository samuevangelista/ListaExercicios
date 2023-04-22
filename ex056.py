somaidade = 0
mediaidade = 0
contmulh = 0
idadevelho = 0
nomevelho = 0
for c in range(1, 5):
    print("============")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()

    somaidade += idade#1°

    if c == 1 and sexo in 'Mn':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

    if idade < 20 and sexo in 'Ff':#3°
        contmulh +=  1


mediaidade = somaidade / 4
print('A media de idade é ', mediaidade)
print('O homem mais velho é o {} com {} anos'.format(nomevelho, idadevelho))
print('Mulheres com menos de 20 anos: {}'.format(contmulh))