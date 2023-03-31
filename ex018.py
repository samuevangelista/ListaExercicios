import math
num = float(input('Digite um angulo que você deseja: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tag = math.tan(math.radians(num))
print('Agngulo dado: {}\n'
      'Sen {:.2f}\n'
      'Cos {:.2f}\n'
      'Tag {:.2f}\n'.format(num, sen, cos, tag))
