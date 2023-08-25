''' Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

import math

num=int(input("Digite um número qualquer: "))
print("Qual será a base de conversão utilizada?\n[1] PARA BINÁRIO\n[2] HEXADECIMAL\n[3] OCTAL")
base=int(input("Opção: "))

if base == 1:
    print(f"O número {num} em binário será {bin(num)[2:]}!")

elif base == 2:
    print(f"O número {num} em hexadecimal será {hex(num)[2:]}!")

elif base == 3:
    print(f"O número {num} em octal será {oct(num)[2:]}!")

else:
    print("Base não reconhecida, tente novamente.")
    exit