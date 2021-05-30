# Faça um programa que leia um número
# e mostre na tela seu antecessor e o seu sucessor.

num = int(input('Digite um número: '))
print('O antecessor de {} é {} e o sucessor de {} é {}.'.format(num, (num-1), num, (num+1)))
