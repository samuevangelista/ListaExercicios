msg = 'PROGRMA ESCOLA'
print('{:=^35}'.format(msg))
nome = input('Nome aluno: ')
n1 = float(input('Primeira nota de {} '.format(nome)))
n2 = float(input('Segunda nota de {} '.format(nome)))
print('='*35)
media = (n1 + n2)/2
print('NOME: {}\n'
      'Nota 1: {}\n'
      'Nota 2: {}\n'
      'Média: {:.1f}\n'.format(nome, n1, n2, media))
