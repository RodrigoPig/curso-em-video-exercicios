# Escreva um programa que converta uma temperatura digitando em graus Fahrenheit  e converta para graus Celsius.
# Formula F = C x 1,8 + 32

temperatura = float(input('Digite uma temperatura: '))

celsus = ((temperatura-32)*5)/9
fahrenheit = ((9 * temperatura)/5)+32

print('A temperatura {} corresponde a {}C°'.format(temperatura,celsus))
print('A temperatura {} corresponde a {}F°'.format(temperatura,fahrenheit))

