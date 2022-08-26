
#Desafio 6
# faça um programa que leia um numero e mostre na tela o seu dobro, o triplo e a raiz quadrada (Dica: 81 **(1/2))

numero = float(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('Voce digitou o numero {}'.format(numero))
print('O dobro de {} é {}'.format(numero, dobro))
print('O triplo de {} é {:.1f}'. format(numero, triplo))
print('A Raiz quadrada de {} é {:.2f}'.format(numero, raiz_quadrada))


