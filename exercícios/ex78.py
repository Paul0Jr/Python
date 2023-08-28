'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

listnum=[]
maior=0
menor=0

for v in range(0,6):
    listnum.append(int(input(f"Informe o valor {v} : ")))
    if v==0:
        maior=menor=listnum[v]
    else:
        if listnum[v]>maior:
            maior=listnum[v]
        if listnum[v]<menor:
            menor=listnum[v]

print(f"O menor valor digitado foi {menor} na posição {listnum.index(menor)+1}")
#print(f"O menor valor digitado foi {min(listnum)} na posição {listnum.index(min(listnum))+1}")
#print(f"O maior valor digitado foi {max(listnum)} na posição {listnum.index(max(listnum))+1}")