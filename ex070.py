print('Loja')
cont = total = 0
preçomenor = 999
while True:
    continuar = 'j'
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += preço
    if preço > 1000:
        cont += 1
    if preço < preçomenor:
        nomemenor = nome
        preçomenor = preço
    if continuar == 'N':
        break
print('FIM DO PROGRAMAM')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} que custa R${preçomenor:.2f}')