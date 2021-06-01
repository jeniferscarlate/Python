# Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário com 15% de aumento.

print('-'*50)
salario = float(input('Digite o salário do funcionário: R$'))
novoSalario = salario + (salario*15/100)


print('O salário de R${:.2f}, com o aumento de 15%,\npassa a ser R${:.2f}.'.format(salario, novoSalario))
print('-'*50)