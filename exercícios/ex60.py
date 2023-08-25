'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

num=int(input("Digite um número: "))
f=num
m=1

while f>0:
    print(f"{f}", end='')
    print(" x " if f>1 else " = ", end="")
    m*=f
    f-=1
print(f"{m}")