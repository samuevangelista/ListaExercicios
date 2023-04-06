dis = int(input('Digite a distancia da sua viagem: '))
if dis <= 200:
    valor = dis * 0.5
    print('O valor da passagem é R${:.f}'.format(valor))
else:
    valor = dis * 0.45
    print('O valor da passagem é R${:.f}'.format(valor))
