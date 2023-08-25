'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
print("Digite sua data de nascimento ")
dia=int(input("Insira o dia: "))
mes=int(input("Insira o número do mês que nasceu: "))
ano=int(input("Insira seu ano de nascimento: "))
atual=date.today().year
idade=atual-ano

if idade==18:
    print("Está na hora exata de se alistar!")
elif idade<18:
    print(f"Ainda é cedo para seu alistamento. Ainda faltam {18-idade}ano(s).")
    print(f"Seu alistamento está previsto para o ano de {atual+(18-idade)}")
else:
    print(f"O seu alistamento está atrasado cerca de {idade-18} ano(s)!")
    print(f"O seu alistámento estava previsto para ser realizado no ano de {atual-(idade-18)}.")


