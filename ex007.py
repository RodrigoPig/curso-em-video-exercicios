# Desafio 7
# escreva um programa que leia duas notas de um aluno calcule e mostre a sua media.

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

media = (nota1 + nota2)/2

if 6.0 <= media <= 6.9:
    print('Sua média é {:.2f}'.format(media))
    print('Parabéns voce passou, porém precisa estudar mais')
elif media < 6.0:
    print('Sua média é {:.2f}'.format(media))
    print('Que pena voce não passou, estude mais na próxima')
elif 7.0 <= media <= 8.9:
    print('Sua média é {:.2f}'.format(media))
    print('Parabéns, voce passou com uma boa média')
elif media >= 9.0:
    print('Sua media é {:.2f}'.format(media))
    print('Parabéns, voce passou com uma excelente média')
