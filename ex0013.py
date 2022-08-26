# Desafio 13
# Escreva um programa que leia o valor do salrio de um funcionario e mostre o seu novo salario com aumento de x% ((salario * aumento)/100)

salario = float(input('Informe o valor do salário do funcionário: '))
aumento = float(input('Informe o valor do aumento (em porcentagem): '))

valor_aumento = (salario * aumento)/100
novo_salario = salario + valor_aumento
print('>'*30)
print('O valor do novo salario é: {:.2f}'.format(novo_salario))
