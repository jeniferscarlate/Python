# Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$'))
novoSalario = salario + (salario*15/100)

print('-'*60)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15%,\npassa a receber R${:.2f}.'.format(salario, novoSalario))
print('-'*60)