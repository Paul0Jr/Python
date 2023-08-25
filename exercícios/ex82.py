'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
   Ao final, mostre o conteúdo das três listas geradas.'''
valores=[]
lpar=[]
limpar=[]
while True:
    user=(input("\nDigite um valor: "))
    if user.isnumeric():   
        user=int(user)
        valores.append(user)
    else:
        print("Digite apenas números!")
        continue
    choice=input("\nDeseja continuar? [S/N]\nSua escolha: ").strip().upper()[0]
    if choice.isalpha():
        if choice in 'SN':
            if choice=='N':
                break
        else:
            print("Responda apenas com 'S' para 'Sim' e 'N' para 'Não'!")
            continue
    else:
        print("Responda apenas com 'S' para 'Sim' e 'N' para 'Não'!")

for i,v in  enumerate(valores):
    if v%2==0:
        lpar.append(v)
    elif v%2==1:
        limpar.append(v)

print(f"A lista digitada completa: {valores}")
print(f"A lista apenas dos números pares: {lpar}")
print(f"A lista apenas dos números ímpares: {limpar}")