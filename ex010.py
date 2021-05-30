# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.
# considere o Dólar 5.23, o Euro 6.37 e Peso mexicano 0.26.

real = float(input('Quantos reais você tem na carteira? R$'))
print('-'*80)
print('Qual moeda você deseja comprar? Digite o equivalente a moeda desejada: ')
moeda = int(input(' (1) Dólar\n (2) Euro\n (3) Peso mexicano\n'))

if moeda == 1:
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, (real / 5.23)))
    print('-' * 80)
elif moeda == 2:
    print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, (real / 6.37)))
    print('-' * 80)
else:
    print('Com R${:.2f} você pode comprar MXN{:.2f}'.format(real, (real/0.26)))
    print('-' * 80)





