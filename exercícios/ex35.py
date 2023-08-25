'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

r1=int(input("Digite o tamanho da primeira reta: "))
r2=int(input("Digite o tamanho da segunda reta: "))
r3=int(input("Digite o tamanho da terceira reta: "))

#DEFININDO SE PODE FORMAR TRIÂNGULO
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f"As medidas {r1}, {r2} e {r3} podem formar um triângulo.")
    
else:
    print("Não é possível formar um triângulo.")