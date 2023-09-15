''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. '''

lista=[]

while True:
    nome=str(input("Insira o nome do aluno: ")).strip().capitalize()
    nota1=float(input(f"Insira a primeira nota de {nome}: "))
    nota2=float(input(f"Insira a segunda nota de {nome}: "))
    media=(nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    user=str(input("\nDeseja adicionar outro aluno(a)? S/N\nSua escolha: ")).upper()
    if user not in "SN":
        user=str(input("\nDeseja adicionar outro aluno(a)? S/N\nSua escolha: ")).upper()
    if user=="N":
        break  
    print("\n")

print(lista)