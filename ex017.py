# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um trângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

print('-'*45)
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdja = float(input('Digite o comprimento do cateto adjacente: '))

hipo = (catOposto * catOposto) + (catAdja * catAdja)
hipo2 = sqrt(hipo)

print('O valor do comprimento da hipotenusa é {:.2f}'.format(hipo2))
print('-'*45)
