'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

nomevelho=''
idadevelho=0
somaidade=0
mulher=0

for i in range(1,5):
    nome=str(input(f"Digite o nome da {i} pessoa: "))
    idade=int(input(f"Digite a idade da {i} pessoa: "))
    sexo=int(input(f"Informe o sexo da {i} pessoa: [1] MASCULINO    [2] FEMININO\nSua escolha: "))
    somaidade+=idade
    if i==1 and sexo==1:
        nomevelho=nome
        idadevelho=idade
    if sexo==1 and idade>idadevelho:
        idadevelho=idade
        nomevelho=nome
    if sexo==2 and idade<20:
        mulher+=1
   
print(f"A média de idade do grupo é igual a {somaidade/4}")
print(f"O homem mais velho possui {idadevelho} anos e se chama {nomevelho}!")
print(f"O total de mulheres abaixo dos 20 anos de idade é {mulher}")