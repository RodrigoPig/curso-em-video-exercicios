# Desafio 8
# Escreva um programa que leia um valor em metros e exiba a conversão em centimetros e milimetros
#  (dica cm *100, milimetros *1000, usar float)

print('Pregrama de converção')
metro = float(input('Digite um valor em metros: '))

centrimetro = metro * 100
milimetro = metro * 1000
print('>'*50)

print('Voce digitou {}'.format(metro))
print('{} metros equivalem a {:.1f} centimetros'.format(metro, centrimetro))
print('{} metros equivalem a {} milimetros'.format(metro, milimetro))
