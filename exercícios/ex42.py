'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1=int(input("Digite o tamanho da primeira reta: "))
r2=int(input("Digite o tamanho da segunda reta: "))
r3=int(input("Digite o tamanho da terceira reta: "))

#DEFININDO SE PODE FORMAR TRIÂNGULO
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f"As medidas {r1}, {r2} e {r3} podem formar um triângulo.")
    if r1==r2 and r1==r3:
        print("Seu triângulo é equilátero.")
    elif r1==r2 and r1!=r3:
        print("Seu triângulo é isósceles.")
    else:
        print("Seu triângulo é escaleno.")
else:
    print("Não é possível formar um triângulo.")