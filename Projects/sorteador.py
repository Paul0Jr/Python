import random
from time import sleep
esc='S'
qtd=[]
while esc=='S':
    jogo=str(input("Digite o nome do jogo que deseja adicionar: ")).strip().title()
    esc1=0
    out=0
    qtd+=[jogo]
    esc=str(input("\nDeseja adicionar outro jogo?\n[S/N]\nSua escolha: ")).upper()


print(f"\nOs jogos sorteados serão: ",end="")
print(", ".join(qtd))
sleep(1)

print("\nDeseja adicionar um cronômetro? ")
cron=str(input("[S/N]\nSua escolha: ")).upper()
print("")
if cron=="S":
    for c in range(6, 0, -1):
        print(f"     {c}")
        print("=-="*5)
        sleep(1)
    print("\nE o jogo sorteado foi: ")
    sleep(0.5)
    print(f"\n\033[32m{random.choice(qtd).upper()}!!\033[32m")
elif cron=="N":
    print("\nE o jogo sorteado foi: ")
    sleep(0.5)
    print(f"\n\033[32m{random.choice(qtd).upper()}!!\033[32m")
    print("=-="*10)

print("\nDeseja sortear novamente? ")
out=str(input("[S/N]\nSua escolha: ")).upper()
while out=="S":
    print("\nE o jogo sorteado foi: ")
    sleep(0.5)
    print(f"\n\033[32m{random.choice(qtd).upper()}!!\033[32m")
    print("\nDeseja continuar? ")
    out=str(input("[S/N]\nSua escolha: "))

print("\nObrigado por usar nosso programa, esperamos que tenha gostado da experiência :)")
sleep(3)
        
