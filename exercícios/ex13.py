'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

nome=input("Digite o nome do funcionário: ")
salario=float(input(f"informe o salário de {nome}: R$"))

print(f"O novo salário de {nome} é igual R${salario+(salario*0.15)}")