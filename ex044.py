print('{:=^40}'.format(' LOJA VENDE MAIS '))
produto = float(input('Digite o preço do produto: '))
condicao = int(input('[1] À vista dinheiro/cheque \n'
                     '[2] À vista cartão          \n'
                     '[3] 2x no cartão            \n'
                     '[4] 3x ou mais no cartão    \n'
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
    parcela = produto / 2
    print('Preço: R${:.2f}'.format(produto))
elif condicao == 4:
    novo = produto * 1.20
    totalparc = int(input('Quantas parcelas?: '))
    parcela = produto / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparc, parcela))
    print('JUROS APLICADO')
    print('Preço Final: R${:.2f}'.format(novo))
else:
   print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente')
