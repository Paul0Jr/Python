'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

ano=int(input("Qual ano deseja saber se é bissexto? "))
if ano % 4 == 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")