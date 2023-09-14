'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.'''

listanum=[[],[]]
for i in range(0,3):
    num=int(input(f"Digite o {i+1} valor: "))
    if num%2==0:
        listanum[0].append(num)
    else:
        listanum[1].append(num)

print("="*30)
print(f"Lista completa dos números digitados: {listanum}")
print(f"Lista apenas com os números pares: {sorted(listanum[0])}")
print(f"Lista apenas com os números ímpares: {sorted(listanum[1])}")