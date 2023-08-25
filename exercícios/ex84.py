'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas;
 B) Uma listagem com as pessoas mais pesadas;
 C) Uma listagem com as pessoas mais leves.'''

pessoas=[]
lista2=[]
pesadas=[]
leves=[]
total=maior=menor=0
while True:
    user=(input("Digite seu nome: ")).strip().capitalize()
    if user.isalpha:
        pessoas.append(user)
    else:
        print("Digite apenas o nome do usuário!")

    peso=input("\nDigite seu peso: ")
    if peso.isnumeric():
        peso=float(peso)
        pessoas.append(peso)
    else:
        print("Por favor, digite apenas o peso do usuário!")   
    total+=1
    if len(lista2)==0:
        maior=menor=pessoas[1]
    else:
        if pessoas[1]>maior:
            maior=pessoas[1]
        if pessoas[1]<menor:
            menor=pessoas[1]

    lista2.append(pessoas[:])
    pessoas.clear()

    
    choice=input("\nDeseja continuar? [S/N]\nSua escolha: ").strip().upper()
    print("")
    if choice.isalpha():
        if choice in 'SN':
            if choice=='S':
                continue
            elif choice=='N':
                break
        else:
            print("Por favor, responda apenas com 'S' para 'Sim' e 'N' para 'Não'\n")
    else:
        print("Por favor, responda apenas com 'S' para 'Sim' e 'N' para 'Não'!\n")


print(f'Foram cadastradas um total de {total} pessoas!')
print(f"O maior peso registrado foi de {maior}, pertencente a ", end="")
for i in lista2:
    if i[1] == maior:
        print(f"{i[0]}")
print(f"O menor peso registrado foi de {menor} pertencente a ", end="")
for i in lista2:
    if i[1] == menor:
        print(f"{i[0]}")
