# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todos sem espaços
# Quantas letras tem o primeiro nome.
# strip() elimina os espaçamentos no inicio e no final da frase
# nome.count(' ') contara o numero de espaços que a fese contem
# (len(nome)-nome.count(' ')) quantidade de caracteres menos a quantidade de espaços
# nome.split() colocara os nomes em uma lista
# primeiro_nome[0] define o nome da posição 0 da lista,
# len(primeiro_nome[0]) conta o numero de letras do item 0 da lista

nome = str(input('Informe o seu nome completo: ')).strip()
nome_maiuscula = nome.upper()
nome_minusculo = nome.lower()
quantidade_de_letras = (len(nome) - nome.count(' '))
primeiro_nome = nome.split()

print( 'Analisando o seu nome ......')
print('O nome {} foi alterado para letras Maiusculas.'.format(nome_maiuscula))
print('O nome {} foi alterado para letras Minusculas.'.format(nome_minusculo))
print('O nome {} possui {} de letras.'.format(nome, quantidade_de_letras))
print('O seu primeiro nome é {} e possui {} de letras.'.format(primeiro_nome[0],len(primeiro_nome[0])))

