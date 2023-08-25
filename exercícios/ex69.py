'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
contid=0
conth=0
contm=0

while True:
    sexo=' '
    esc=' '
    idade=int(input("Digite sua idade: ")) 
    while sexo not in 'MF':
        sexo=str(input("\nDigite seu sexo: ")).strip().upper()[0]
    if idade>=18:
        contid+=1
    if sexo=="M":
        conth+=1
    elif sexo=="F" and idade<20:
         contm+=1
    while esc not in 'SN':
        esc=str(input("\nDeseja continuar?\nSua escolha: ")).strip().upper()[0]
    if esc=="N":
        break
print(f"\nForam cadastradas pessoas!\n{contid} pessoa(s) tem mais de 18 anos\n{conth} homens foram cadastrados\n{contm} mulheres têm menos de 20 anos")
        
        
        
