'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

tuple=()
listwords=tuple

while True:
    user=input("Digite alguma palavra sem acento: ")
    if user.isalpha():
        tuple+=(user,)
    else:
        print("Digite apenas palavras!")
    choice=input("\nDeseja continuar adicionando palavras? [S/N]\nSua escolha: ").upper()
    print("")
    if choice.isalpha():
        if len(choice)>1:
            print("Responda apenas com 'S' para 'Sim' e 'N' para 'Não'.")
        else:
            if choice=='S':
                continue
            elif choice=='N':
                break
            else:
                print("Responda apenas com 'S' para 'Sim' e 'N' para 'Não'.")
    else:
        print("Responda apenas com 'S' para 'Sim' e 'N' para 'Não'.")

for p in tuple:
    print(f"Para a palavra {p}, temos: ",end='')
    for vog in p:
        if vog.lower() in 'aeiou':
            print(vog, end="")
    print("")
        