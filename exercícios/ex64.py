'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
num=0
soma=num
cont=0

num=int(input("Digite um número: "))
while num!=999:
    cont+=1
    soma+=num
    num=int(input("Digite um número: "))
print(f"A soma total entre os {cont-1} números digitados é de {soma}")