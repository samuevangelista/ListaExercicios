from datetime import date
ano = int(input('Digite um ano qualquer!Digite 0 se quiser o nao atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano  % 400 == 0:
    print('O ano {} é BISEXTO0'.format(ano))
else:
    print('O ano {} não é BISEXTO'.format(ano))