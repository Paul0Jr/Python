'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel=int(input("Qual a velocidade que o carro estava? "))

if vel>80:
    print(f"Excesso de velocidade excedido! Será aplicada uma multa de R${(vel-80)*7}.")

else:
    print("Velocidade aceitável, sem cobrança de multa.")