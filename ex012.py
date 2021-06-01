# Faça um algoritmo que leia o preço de um produto e mostre seu novo
# preço com 5% de desconto.

produto = float(input('Digite o preço do produto: R$'))
desconto = (produto*5)/100
comDesconto = (produto - desconto)

print('O preço do produto é R${:.2f}, com desconto de 5% vai custar R${:.2f}.'.format(produto, comDesconto))