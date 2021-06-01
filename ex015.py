# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

print('-'*45)
km = float(input('Quantos Km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

total = (km*0.15)+(dias*60)
print('O total a ser pago é R${:.2f}.'.format(total))
print('-'*45)
