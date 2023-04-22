from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 4):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('{} já atingiram a maior idade, {} ainda não atingiram'.format(maior, menor))