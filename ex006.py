# crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e sua raiz quadrada.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)

print('O dobro de {} é igual a {}.'.format(num, dobro))
print('O triplo de {} é igual a {}.'.format(num, triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, raizq))
