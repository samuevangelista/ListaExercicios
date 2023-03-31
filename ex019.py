import random

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
a5 = input('Digite o nome do 5° aluno: ')

lista = [a1, a2, a3, a4, a5]

escolha = random.choice(lista)

print('O aluno escolhido foi {}' .format(escolha))

'''cont = random.randint(1, 5)
if cont == 1:
    print('O aluno escolhido foi o {}'.format(a1))
elif cont == 2:
    print('O aluno escolhido foi o {}'.format(a2))
elif cont == 3:
    print('O aluno escolhido foi o {}'.format(a3))
elif cont == 4:
    print('O aluno escolhido foi o {}'.format(a4))
else:
    print('O aluno escolhido foi o {}'.format(a5))'''

