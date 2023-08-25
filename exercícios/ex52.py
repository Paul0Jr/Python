'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num=int(input("Digite um número aleatório: "))
total=0

for i in range(1, num+1):
    if num % i == 0:
        print("\033[32m", end=" ")
        total+=1
    else:
        print("\033[31m", end= " ")
    print(i, end=" ")
print(f"\n\033[37mO número {num} é divísivel por {total} número(s)\033[37m")
print(f"O número {num} é primo!" if total==2 else f"O número {num} não é primo!")