km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Por quantos dias ele foi alugado? '))
km = km * 0.15
dias = dias * 60
total = km + dias
print('O total a pagar é de R${:.2f}'.format(total))
