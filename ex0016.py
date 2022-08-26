# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

numero = float(input('Escreva um numero inteiro: '))

print('O numero digitado foi {} e sua porção inteira é {}'.format(numero, trunc(numero)))


# outra forma de fazer sem a biblioteca

''' numero = float(input('Escreva um numero inteiro: '))

print('O numero digitado foi {} e sua porção inteira é {}'.format(numero, int(numero))) '''