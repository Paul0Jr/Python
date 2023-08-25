'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km=int(input("Informe quantos quilômetros foram rodados com o carro: "))
dias=int(input("Informe por quantos dias o carro foi alugado: "))

print(f"O total a ser pago pelos {km}km rodados e {dias} dia(s) que o carro foi alugado será de {dias*60+km*0.15}!")