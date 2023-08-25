'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual=date.today().year
print(atual)
maior=0
menor=0

for i in range(1, 8):
    ano=int(input(f"Insira a data de nascimento da {i}° pessoa: "))
    if atual-ano>=18:
        maior+=1
    else:
        menor+=1
print(f"{maior} pessoa(s) são maiores de idade, e {menor} pessoa(s) ainda são menores de idade!")