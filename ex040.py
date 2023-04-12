n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A media alcançada foi {}'.format(m))
if m < 5.0:
    print('O aluno está REPROVADO')
elif m >= 5.0 and m <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O auno está APROVADO')

