'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print("=-= "*5, end="")
print("CALCULADORA DE PROGRESSÃO DE ARIMÉTICA", end="")
print(" =-="*5)
num=int(input("\nDigite o primeiro valor de sua P.A: "))
raz=int(input("Insira o valor de sua razão: "))
enes=int(input("Informe o seu enésimo termo: "))
termo=num
cont=1

while cont<=enes:
    print(f"{termo} ", end="")
    print("-> " if cont<enes else "", end="")
    cont+=1
    termo+=raz