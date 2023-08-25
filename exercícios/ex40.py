'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1=float(input("Insira a primeira nota do aluno: "))
n2=float(input("Insira a segunda nota do aluno: "))
media=(n1+n2)/2

if media>=7.0:
    print("APROVADO!")
elif 7>media>=5.0:
    print("RECUPERAÇÃO!\nRestaram {:.1f} para o aluno ser aprovado direto.".format(7.0-media))
else:
    print("REPROVADO!\nFaltaram {:.1f} para o aluno entrar de recuperação e {:.1f} para ser aprovado direto.".format(5.0-media, 7.0-media))