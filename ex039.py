from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Vc está com {}'.format(idade))
if idade < 18:
    idade = 18 - idade
    print('Você ainda deverá se alistar, daqui a {} ano'.format(idade))
elif idade == 18:
    print('Está na hr de se alistar')
else:
    idade = idade - 18
    print('Já passou o prasso de vc se alistar em {}'.format(idade))

