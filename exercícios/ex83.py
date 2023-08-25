'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

listap=[]

user=input("Digite alguma expressão entre parênteses: ").strip()
listap.append(user)

for simb in user:
    if simb=='(':
        listap.append('(')

    elif simb==')':
        if len(listap)>0:
            listap.pop()
        else:
            listap.append(')')
            break

if len(listap)==0:
    print(f"Sua expressão é válida!")
else:
    print(f"Sua expressão é inválida!")