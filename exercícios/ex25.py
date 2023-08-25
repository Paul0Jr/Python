'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome=input("Digite seu nome completo: ").strip()

print("Seu nome possui Silva?: {}".format('SILVA' in nome.upper()))