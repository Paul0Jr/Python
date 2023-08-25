'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

a1=input("Digite o nome do primeiro(a) aluno(a): ")
a2=input("Digite o nome do segundo(a) aluno(a): ")
a3=input("Digite o nome do terceiro(a) aluno(a): ")
a4=input("Digite o nome do quarto(a) aluno(a): ")

lista=[a1, a2, a3, a4]
random.shuffle(lista)

print("A ordem de apresentaçao será a seguinte: ")
print(lista)