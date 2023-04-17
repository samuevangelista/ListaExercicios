from datetime import date
maior = 0
menor = 0
for c in range(1, 4):
    ano = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('{} já atingiram a maior idade, {} ainda não atingiram'.format(maior, menor))