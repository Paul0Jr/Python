'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.'''

cidade=input("Em qual cidade nasceu?: ").strip()

print(cidade[:5].upper() == 'SANTO')
