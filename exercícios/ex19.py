'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

a1=input("insira o nome do primeiro(a) aluno(a): ")
a2=input("Insira o nome do segundo(a) aluno(a): ")
a3=input("Insira o nome do terceiro(a) aluno(a): ")
a4=input("Insira o nome do quarto(a) aluno(a): ")

lista=[a1, a2, a3, a4]

print("O aluno(a) sorteado foi: {}!".format(random.choice(lista)))