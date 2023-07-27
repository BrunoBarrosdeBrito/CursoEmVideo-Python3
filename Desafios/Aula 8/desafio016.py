#Crie um programa que leia um número Real qualquer pelo teclado e mostre na sua tela a sua porção inteira. 
#Ex: Digite um número:6.127
#O número 6.127 tem a parte inteira 6.

'''import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))'''

'''from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira e {}'.format(num, int(num)))