# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa. (teorema de pitagoras)

from math import hypot

cateto_oposto = float(input('Digite o valor do Cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(cateto_adjacente, cateto_oposto) # ao importar somente o hypot, não precisa colocar o math (math.hypot)

print('O valor da hipotenusa para os catetos {} e {} é: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))

