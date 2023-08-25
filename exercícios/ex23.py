'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num=int(input("Digite seu número: "))
n1=str(num)

print(f"Casa do milhar: {n1[0]}")
print(f"Casa da centena: {n1[1]}")
print(f"Casa da dezena: {n1[2]}")
print(f"Casa da unidade: {n1[3]}")