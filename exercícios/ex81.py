'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
A) Quantos números foram digitados; 
B) A lista de valores, ordenada de forma decrescente; 
C) Se o valor 5 foi digitado e está ou não na lista.'''

cont=0
nums=[]
while True:
    user=input("Digite algum valor: ")
    if user.isnumeric:
        if user not in nums:
            nums.append(user)
            cont+=1
    else:
        print("Digite apenas números!")
    choice=input("Deseja continuar? [S/N]\nSua escolha: ").strip().upper()[0]
    if choice.isalpha:
        if choice=='S':
            continue
        elif choice=='N':
            break
    else:
        print("Digite apenas 'S' para 'Sim' e 'N' para 'Não'!")

print(f"Foram digitados {cont} números")
print(f"a lista {nums} em ordem decrescente é {nums.sort(reverse=True)}")
if 5 in nums:
    print(f"O número 5 foi digitado na posição {nums.index('5')+1}")
else:
    print("O número 5 não foi digitado.")