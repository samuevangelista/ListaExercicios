produto = float(input('Digite o preço do produto: '))
condicao = int(input('À vista dinheiro/cheque [1]\n'
                     'À vista cartão          [2]\n'
                     '2x no cartão            [3]\n'
                     '3x ou mais no cartão    [4]\n'
                     'ESCOLHA: '))
if condicao == 1:
    novo = produto * 0.9
    print('DESCONTO APLICADO')
    print('Preço: R${:.2f}'.format(novo))
elif condicao == 2:
    novo = produto * 0.95
    print('DESCONTO APLICADO')
    print('Preço: R${:.2f}'.format(novo))
elif condicao == 3:
    print('NENHUM DESCONTO APLICADO')
    print('Preço: R${:.2f}'.format(produto))
elif condicao == 4:
    novo = produto * 1.20
    print('JUROS APLICADO')
    print('Preço: R${:.2f}'.format(novo))

