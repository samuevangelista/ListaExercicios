print('\033[7;30;44m--EMPRESTIMO BANCÁRIO--\033[m')
casa = float(input('Qual o valor da casa ?: R$'))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
meses = anos * 12
prestacao = casa / meses

if salario * 0.3 >= prestacao:
    print('EMPRESTIMO AUTORIZADO!')
    print('{} prestações de R${:.2f} cada'.format(meses, prestacao))
else:
    print('EMPRESTIMO NEGADO')
    print('{} prestações de R${:.2f} cada'.format(meses, prestacao))
    print('A prestação ultrapassou 30% do seu salário.')