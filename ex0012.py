# Desafio 12
# Escreva um programa que leia o preço de um produto e mostre o valor com 5% ((valor_produto * 5)/100) de desconto

valor_produto = float(input('Informe o valor do produto: '))
# desconto de 5%
desconto = (valor_produto * 5 / 100)

valor_com_desconto = valor_produto - desconto
print('O valor do produto é {:.2f}'.format(valor_produto))
print('Valor com 5% de desconto {}'.format(valor_com_desconto))
