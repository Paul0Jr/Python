'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

parent=[]
frase=str(input("Digite uma expresão utilizando parênteses: "))

for simb in frase:
    if simb=="(":
        parent.append("(")
    elif simb==")":
        if len(parent)>0:
            parent.pop()
        else:
            parent.append(")")

            break

if len(parent) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")