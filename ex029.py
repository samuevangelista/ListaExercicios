print('=== DETRAN ===')
v = int(input('Digite a velocidade do carro em Km/h: '))
if v <= 80:
    print('Tudo Certo!')
else:
    print('O carro escedeu o limite de veocidade à {}Km/h.'.format(v))
    v = v - 80
    m = v * 7
    print('Valor da multa a ser pago: R${},00'.format(m))
