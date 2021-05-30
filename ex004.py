num1 = int(input('Digite um valor: '))
num2 = int(input('Digite mais um valor: '))
soma = num1 + num2
sub = num1 - num2
div = num1 / num2
multi = num1 * num2
divInt = num1 // num2
ex = num1 ** num2

print('A soma vale {}, a subtração é igual a {} e a divisão é {:.2f}.'.format(soma, sub, div), end=' ')
print('O produto é {}, a divisão inteira é {} e a potência é {}.'.format(multi, divInt, ex))
