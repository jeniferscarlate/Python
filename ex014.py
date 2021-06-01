# Escreva uma programa que converta uma temperatura digitada em ºC para ºF.

print('-'*50)
tempC = float(input('Digite a temperatrura em graus celsius: '))
tempF = (tempC * 1.8)+32

print('A temperatura de {}ºC equivale a {}ºF'.format(tempC, tempF))
print('-'*50)