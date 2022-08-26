# Desafio 10
#  - escreva um programa onde o usuaria digite um valor em reais e mostre quanto ele pode comprar em dolares

reais = float(input('informe o valor, em Reais, pra a conversão: '))
convercao = reais / 5.67

print('-'*50)
print('R$ {} Reais, vale U$ {:.2f} Dolares'.format(reais, convercao))
