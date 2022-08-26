# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Informe o valor do ângulo: '))

# conferter os graus para radianos (math.radians(angulo))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo {}° possui Seno de {:.2f}, Cosseno de {:.2f} e Tangente de {:.2f}.'.format(angulo, seno, cosseno, tangente))