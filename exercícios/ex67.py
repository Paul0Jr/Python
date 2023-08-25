'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''

num=int(input("Digite o número que deseja ver a tabuada: "))
print("=-="*12)
while True:
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    print("=-="*12)
    num=int(input("Digite o número que deseja ver a tabuada: "))
    if num<0:
        break
print("\nPROGRAMA ENCERRADO! OBRIGADO POR UTILIZAR :)")