'''import math
cat1 = float(input('Digite o comprimento de um lado do triangulo:'))
cat2 = float(input('Digite o comprimento do outro lado do triangulo:'))
hip = cat1 * cat2
print('Com um triangulo de catetos {} e {}, a hipotenusa {:.2f}'.format(cat1, cat2 , math.hypot(cat1,cat2)))'''

from math import hypot
cat1 = float(input('Digite o comprimento de um lado do triangulo:'))
cat2 = float(input('Digite o comprimento do outro lado do triangulo:'))
hip = hypot(cat1,cat2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
