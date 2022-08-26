# Desafio 11
# escreva um programa que leia a largura e a altula de uma parede (em metros), calcule a area dessa parede e quanto vai gastar de
# tinta para pintar, sabendo que cada litro de tinta pinta 2m².

largura = float(input('Informe a Largura da parede (um metros): '))
altura = float(input('Imforme a Altura da parede (em metros): '))

area_da_parede = largura * altura
print('A área total da parde é {} M²'.format(area_da_parede))

litro_tinta = area_da_parede / 2

print('Voce ira precisar de {} litros de tinta'.format(litro_tinta))
