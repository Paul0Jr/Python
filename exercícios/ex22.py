'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome=input("Digite seu nome completo: ")
nome.strip()

primeiro=nome.split()

print(f"Seu nome em letras maísculas é {nome.upper()}.")
print(f"Seu nome em letras minúsculas é {nome.lower()}.")
print(f"Seu nome possui um total de {len(nome) - nome.count(' ')} letras.")
print(f"Seu primeiro nome é {primeiro[0]} e possui {len(primeiro[0])} letras.")