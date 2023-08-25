'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal=float(input("Qual o salário do funcionário? "))

#PARA SALÁRIOS ACIMA DE R$1250,00
if sal>1250.00:
    aumento=sal+(sal*0.1)
    print("Com um aumento de 10% baseado no seu salário, sua remuneração atual será de R${:.2f}.".format(aumento))
else:
    aumento=sal+(sal*0.15)
    print("Com um aumento de 15% baseado no seu salário, sua remuneração atual será de R${:.2f}.".format(aumento))