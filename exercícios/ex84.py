'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas;
 B) Uma listagem com as pessoas mais pesadas;
 C) Uma listagem com as pessoas mais leves.'''

cadastro=[]
dados=[]
cont=0
while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite seu peso: ")))
    cadastro.append(dados[:])
    dados.clear()
    cont+=1
    esc=str(input("Deseja continuar? S/N")).upper()
    if esc in "SN":
        if esc=='N':
            break
    else:
        print("Responda apenas com S para Sim e N para Não!")
        esc=str(input("Deseja continuar? S/N")).upper()

print(cadastro)