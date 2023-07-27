'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h1))'''

'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimetno do cateto adjacente: '))
h1 = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h1))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h1))