# Desafio 5
# faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o antecessor

numero = int(input('Digite um numero inteiro: '))
sucessor = numero + 1
antecessor = numero - 1

print('Voce digitou o numero {}'.format(numero))
print('O sucessor do numero {} é {}'.format(numero, sucessor))
print('O antecessor do numero {} é {}'.format(numero, antecessor))
