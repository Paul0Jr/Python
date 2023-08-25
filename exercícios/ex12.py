'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco=float(input("Informe o preço do produto: "))
desconto=int(input("Informe a porcentagem do desconto: "))

print(f"O valor final do seu produto será de R${preco-(preco*(desconto/100))}")