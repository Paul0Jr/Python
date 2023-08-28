'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

listanum=list()

while True:
    num=int(input("Digite o número que deseja adicionar na lista: "))
    if num not in listanum:
        listanum.append(num)
    else:
        print("Número duplicado, não irei adicionar!")
    choice=input("Deseja continuar? S/N").upper()
    if choice not in "SN":
        print("Por favor, só responda com S para Sim e N para Não!")
        choice=input("Deseja continuar? S/N").upper()
    else:
        if choice=="N":
            break

print(sorted(listanum))