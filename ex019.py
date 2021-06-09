# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça
# um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
print('-'*50)
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}.'.format(escolhido))
print('-'*50)
