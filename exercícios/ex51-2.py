
#DEFININDO VARIÁVEIS
num=int(input("Digite o primeiro termo: "))
raz=int(input("Digite sua razão: "))
enes=int(input("Digite seu enésimo termo: "))
pg=num*(raz**(enes-1))

for i in range(num, pg+1, raz**(enes-1)):
    print(i)
