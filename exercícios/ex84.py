'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas;
 B) Uma listagem com as pessoas mais pesadas;
 C) Uma listagem com as pessoas mais leves.'''

cadastro=[]
dados=[]
leve=pesado=0
while True:
    nome=str(input("\nDigite seu primeiro nome: ")).capitalize().strip()
    dados.append(nome)
    peso=float(input("Digite seu peso: "))
    dados.append(peso)
    if len(dados)==0:
        leve=pesado=dados[1]
    else:
        if dados[1]>pesado:
            pesado=dados[1]
        if dados[1]<leve:
            leve=dados[1]
    cadastro.append(dados[:])
    dados.clear()
    esc=str(input("\nDeseja continuar? S/N\nSua escolha: ")).upper()
    if esc in "SN":
        if esc=='N':
            break
    else:
        print("Responda apenas com S para Sim e N para Não!")
        esc=str(input("Deseja continuar? S/N")).upper()

# print(cadastro)
print(f"Foram registradas {len(cadastro)} pessoas!")
print(f"A lista com as pessoas mais leves é formada por: ")
