'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

preco=float(input("insira preço do produto: "))
metodo=int(input("Escolha o método de pagamento: \n[1] à vista dinheiro/cheque\n[2] cartão\n Escolha: "))

#DEFININDO MÉTODO
if metodo==1:
    print("O valor final do produto, com 10% de desconto aplicado será de R${:.2f}".format(preco-(preco*0.1)))
elif metodo==2:
    cartao=int(input("Escolha em quantas vezes deseja parcelar: \n[1] à vista\n[2] 2x no cartão\n[3] 3x ou mais no cartão\nEscolha: "))
    if cartao==1:
        print("O valor final do produto, com 5% de desconto aplicado será de R${:.2f}".format(preco-(preco*0.05)))
    elif cartao==2:
        print("O valor final do produto, sem aplicação de descontos será em {} vezes de R${:.2f}.\nValor final: R${:.2f}".format(cartao, preco/2, preco))
    elif cartao==3:
        parc=int(input("Informe em quantas vezes deseja parcelar: "))
        print("O valor final do produto, com 20% de juros aplicado será em {} vezes de R${:.2f}.\nValor final: R${:.2f}".format(parc, (preco+(preco*0.2))/parc, preco+(preco*0.2)))