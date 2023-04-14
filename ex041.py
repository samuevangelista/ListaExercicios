from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('O atleta está com {} anos'.format(idade))
if idade <= 9:
    print('De acordo com a idade, o atleta entra na categoria MIRIM')
elif idade <= 14:
    print('De acordo com a idade, o atleta entra na categoria INFANTIL')
elif idade <= 19:
    print('De acordo com a idade, o atleta entra na categoria JUNIOR')
elif idade == 20:
    print('De acordo com a idade, o atleta entra na categoria SÊNIOR')
elif idade > 20:
    print('De acordo com a idade, o atleta entra na categoria MASTER')
