'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

num=int(input("Digite o primeiro termo de sua PA: "))
raz=int(input("Digite a razão de sua PA: "))
enes=int(input("Digite o seu enésimo termo: "))
pa= num+(enes-1)*raz

for i in range(num, pa+1, raz):
    print(i)