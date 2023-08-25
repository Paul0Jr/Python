'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''


cont=1
num=int(input("Digite um número(999 para parar): "))
soma=num
while True:
    num=int(input("Digite um número(999 para parar): "))
    if num==999:
        break
    cont+=1
    soma+=num
    
    
print(f"a soma total entre os {cont} valores digitados é {soma}")
