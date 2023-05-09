valores=[]
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    resp = 'j'
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('='*40)
valores.sort()
print(f'Você digitouo os valores {valores}')