'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))

#IDENTIFICANDO O MENOR
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

#IDENTIFICANDO O MAIOR
if n1>n2 and n1>n3:
    print(f"O número {n1} o é maior e {menor} é o menor.")
elif n2>n1 and n2>n3:
    print(f"O número {n2} é o maior e {menor} é o menor.")
else:
    print(f"O número {n3} é o maior e {menor} é o menor.")
