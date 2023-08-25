'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print("=-="*15)
print("DESAFIO DO ÍMPAR OU PAR")
print("=-="*15)


while True:
    cont=0
    pc=randint(0,10)
    esc=str(input("\nEscolha entre ímpar ou par: ")).strip().upper()[0]
    while esc not in "PI":
        esc=str(input("Escolha entre ímpar ou par: ")).strip().upper()[0]
    user=int(input("Escolha um número: "))
    soma=user+pc
    print(f"Eu escolhi {pc} e você escolheu {user}")
    if esc=="I":
        if soma%2==1:
            print("VOCÊ VENCEU!!\nVAMOS DE NOVO\n")
        else:
            break
    elif esc=="P":
        if soma%2==0:
            print("VOCÊ VENCEU!!\nVAMOS DE NOVO\n")
            cont+=1
        else:
            break
print(f"\nParece que você finalmente perdeu. Você ainda conseguiu ganhar {cont} partidas seguidas!")