'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.'''

lista=[[], []]
totpar=totimpar=0

for i in range(1,8):
    valores=int(input(f"Digite o {i}º valor: "))
    if valores%2==0:
        lista[0].append(valores)
        totpar+=1
    elif valores%2==1:
        lista[1].append(valores)
        totimpar+=1

print(f"Foram digitados um total de {totpar} números pares, sendo eles: {sorted(lista[0])}")
print(f"Foram digitados um total de {totimpar} números ímpares, sendo eles: {sorted(lista[1])}")