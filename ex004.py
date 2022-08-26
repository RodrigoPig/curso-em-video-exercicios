# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.
from unicodedata import numeric

digitado = input('Digite algo: ')

if not digitado:
    print('Você não digitou nada, tente novamente..')
else:
    print('Voce digitou algo? {}'.format(digitado.isalnum()))
    print('O tipo primitivo desse valor é: {}'.format(type(digitado)))
    print('A palavra esta em Maiuscula? {}'.format(digitado.isupper()))
    print('A palavra esta em Maiuscula? {}'.format(digitado.islower()))
    print('voce digitou um numero? {}'.format(digitado.isnumeric()))





