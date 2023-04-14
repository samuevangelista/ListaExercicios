peso = int(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('Com o imc {:.1f}, indica que vc está ABAIXO DO PESO'.format(imc))
elif 18.5 <= imc < 25:
    print('Com o imc {:.1f}, indica que vc está no PESO IDEAL'.format(imc))
elif 25 <= imc < 30:
    print('Com o imc {:.1f}, indica que vc está com SOBREPESO'.format(imc))
elif 30 <= imc < 40:
    print('Com o imc {:.1f}, indica que vc está com OBESIDADE'.format(imc))
else:
    print('Com o imc {:.1f}, indica que vc está com OBESIDADE MÓRBIDA'.format(imc))