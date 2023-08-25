'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

n=int(input("Digite o número de termos que deseja que seja mostrado na tela: "))
a=0
b=1
cont=3
print(f"{a} -> {b}",end="")

while cont<=n:
    c=a+b
    print(f" -> {c}", end="")
    a=b
    b=c
    cont+=1
print(" -> FIM")