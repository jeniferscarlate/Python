# Crie um programa que leia um número real qualquer pelo teclado e mostre na
# tela a sua  porção inteira.

from math import trunc
print('-'*35)
num = float(input('Digite um número real: '))
print('A porção inteira de {} é {}.'.format(num, trunc(num)))
print('-'*35)
