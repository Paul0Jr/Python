''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta. '''

from random import randint
lista_composta=[]
jogos=int(input("Digite a quantidade de jogos que serão gerados: "))

#Adicionando listas na lista
for listas in range(jogos):
    lista_composta+=[[0,0,0,0,0,0]]

#print(pc)
#print(lista_composta)