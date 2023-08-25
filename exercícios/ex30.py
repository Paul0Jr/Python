''' Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

num=int(input("Digite um número:"))
print(f"O número {num} é par." if num % 2 ==0 else f"O número {num} é ímpar." )