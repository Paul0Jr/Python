'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.'''

listanum=[]
principal=[]
for i in range(0,6):
    listanum.append(int(input(f"Digite o {i} valor: ")))
    
    if listanum[i]%2==0:
        principal.append(listanum)
    

print(principal)