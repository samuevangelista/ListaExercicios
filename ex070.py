print('Loja')
cont = totmil = total = 0
preçomenor = 999
while True:
    continuar = ' '
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        preçomenor = preço
        nomemenor = nome
    else:
        if preço < preçomenor:
            preçomenor = preço
            nomemenor = nome
    if continuar == 'N':
        break
print('FIM DO PROGRAMAM')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} que custa R${preçomenor:.2f}')