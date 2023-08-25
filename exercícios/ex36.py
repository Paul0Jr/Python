''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa=float(input("Insira o valor total da casa: "))
salario=float(input("Insira o salário do comprador: "))
anos=int(input("Insira a quantidades de anos que o comprador pagará a casa: "))

#DEFININDO O CÁLCULO DA PRESTAÇÃO
prestacao=casa/(anos*12)

#CRIANDO A CONDICIONAL DA PRESTAÇÃO
if prestacao <= salario*0.3:
    print("Parabéns seu empréstimo bancário foi aceito!\nSua prestação mensal será de R${:.2f}!".format(prestacao))
else:
    print("Como o valor da prestação execedeu 30% de seu salário, no caso R${:.2f}, não poderemos aceitar seu empréstimo bancário.".format(salario*0.3))