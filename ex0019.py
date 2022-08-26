# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = input('Primeiro aluno(a): ')
aluno2 = input('Segundo aluno(a): ')
aluno3 = input('Terceiro aluno(a): ')
aluno4 = input('Quarto aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]

# metodo choice escole um elemento da lista

sorteio = choice(lista)

print('O aluno sorteado foi: {}'.format(sorteio))

