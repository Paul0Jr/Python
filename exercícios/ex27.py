'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome=input("Digite seu nome completo: ").strip().title()
n=nome.split()

print(f"Seu primeiro nome é {n[0]} e seu último nome é {n[len(n)-1]}")
