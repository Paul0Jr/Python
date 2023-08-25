'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:

    A) qual é o total gasto na compra.

    B) quantos produtos custam mais de R$1000.

    C) qual é o nome do produto mais barato.'''

preco=0
cont=barato=caro=0
nomeb=' '
nomec=' '
soma=preco
tot1000=0

while True:
    nome=' '
    esc=' '
    nome=str(input("Digite o nome do produto: ")).strip()
    preco=float(input("Digite o preço do produto: "))
    soma+=preco
    cont+=1
    while esc not in 'SN':
        esc=str(input("\n Deseja continuar a compra? ")).strip().upper()[0]
    if cont==1:
        if preco>0:
            caro=preco
            nomec=nome
            barato=preco
            nomeb=nomec
    else:
        if preco<barato:
            barato=preco
            nomeb=nome
    if preco<1000:
        tot1000+=1
    if esc=='N':
        break
print(f"O total gasto foi de {soma}\n{tot1000} saíram abaixo de R$1000\n{nomec} foi o produto mais caro, custando R${caro}\n{nomeb} foi o produto mais barato, custando R${barato}")
