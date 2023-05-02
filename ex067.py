while True:
    tabuada = int(input('Quer ver a tabua de qual valor? '))
    print('-' * 20)
    if tabuada <= 0:
        break
    c = 1
    while c <= 10:
        print(f'{tabuada} x {c} = {(tabuada * c)}')
        c += 1
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')