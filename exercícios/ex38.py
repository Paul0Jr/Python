'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1=int(input("Insira o primeiro número: "))
n2=int(input("insira o segundo número: "))

#COMPARANDO OS NÚMEROS
if n1>n2:
    print("O primeiro valor é maior.")
elif n1<n2:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")