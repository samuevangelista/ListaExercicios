salario = float(input('Digite o valor do seu salário: '))
if salario > 1250.00:
    salario = salario * 1.1
    print('O seu salário reajustado será R${}'.format(salario))
else:
    salario = salario * 1.15
    print('O seu salário reajustado será R${}'.format(salario))