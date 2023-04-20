somaidade = 0
contmulh = 0
idadevelho = 0
nomevelho = 0
for c in range(1, 5):
    print("============")
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = input('''SEXO
[ 1 ] Masculino
[ 2 ] Feminino
Escolha: ''')

    somaidade += idade#1°

    if sexo == 1 and idade > idadevelho:#2°
        idadevelho = idade
        nomevelho = nome

    if idade < 20 and sexo == 2:#3°
        contmulh +=  1


somaidade = somaidade / 4
print('A media de idade é ', somaidade)
print('O homem mais velho é o {} com {} anos'.format(nomevelho, idadevelho))
print('Tem {} mulheres com menos de 20 anos'.format(contmulh))