'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep

pc=randint(0,10)
print('\033[34m=-=\033[34m'*10)
print("\033[32m     JOGO DA ADIVINHAÇÃO\033[33m")
print('\033[34m=-=\033[34m'*10)
print("\033[37mAdivinhe o número que estou pensando!")
user=int(input("Seu número: "))

contador=1
tent=0

#CASO O NÚMERO NÃO PERTENÇA A (0,10)
while user not in range(0,10):
    print("\n\nNúmero inválido. Escolha apenas um número entre 0 a 10!")
    sleep(1.2)
    user=int(input("Seu número: "))
    tent+=1
    if tent>=5:
        print("Parece que alguém está tentando me irritar! Cansei de jogar com você, tchau!")

#CASO O USUÁRIO ERRE O NÚMERO DA MÁQUINA
while user != pc:
    contador+=1
    print(f"HAHAHA! PARECE QUE VOCÊ ERROU! Eu pensei no {pc} e você escolheu {user}!")
    user=int(input("\nDigite outro número: "))

if user==pc:
    print(f'Eu pensei no {pc} e você também escolheu {user}!\nParabéns, você finalmente acertou o número!\n')
    print(f"Foram {contador} tentativas até finalmente acertar o número!")