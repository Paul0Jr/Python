'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

print("=====TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO======")
comp=randint(0,5)

numero=int(input("Digite o número que estou pensando: "))
print("PROCESSANDO...")
sleep (2)
if numero == comp:
    print(f"Parabéns, você pensou no número {numero} e eu pensei no número {comp}. Você me venceu :)")
else:
    print(f"Oh que pena, você pensou no número {numero} e eu pensei no número {comp}. Tente novamente :(")