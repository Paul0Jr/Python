'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from time import sleep
from random import randint

print("\033[34m====VAMOS JOGAR JOKENPÔ===\033[m")

user=int(input("Escolha entre pedra, papel e tesoura: \n[1]\033[033m PEDRA\033[m\n[2]\033[34m PAPEL\033[m\n[3]\033[35m TESOURA\033[m\n\nSua escolha: "))

pc=randint(1,3)
lista=('Pedra', 'Papel', 'Tesoura')
print("PROCESSANDO...")
sleep(1.5)

print("Você jogou {}".format(lista[user]))
sleep(1)
print("O computador jogou {}\n".format(lista[pc]))
sleep(0.5)
if user==pc:
    print("Hmmm parece que empatamos. Vamos de novo.")
else:
    if user==1 and pc==2:
        print("Papel cobre a pedra. Eu ganhei de você HAHAHA\n\n\033[32mTente novamente :)\033[32m")
    elif user==2 and pc==1:
        print("Ah droga, papel cobre a pedra. você ganhou!\n\n\033[31mVAMOS NOVAMENTE >:(\033[31m")
    elif user==3 and pc==1:
        print("Pedra destrói a tesoura. EU GANHEI DESSA VEZ HAHAHA\n\n\033[32mNão fique triste, tente novamente :)\033[32m")
    elif user==1 and pc==3:
        print("NÃO!! Pedra quebra tesoura. Você me venceu!\n\n\033[31mVAMOS UMA REVANCHE!!\033[31m")
    elif user==2 and pc==3:
        print("É ISSO!! Eu lhe picotei pois tesoura corta papel HAHAHA\n\n\033[32mTente me vencer :)\033[32m")
    elif user==3 and pc==2:
        print("NÃO É POSSÍVEL! Eu perdi pois você cortou meu papel com sua tesoura.\n\n\033[31mNÃO ACEITO PERDER, VAMOS OUTRA RODADA >:(\033[31m")