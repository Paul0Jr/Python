'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print("=-= "*8)
print("CALCULADORA DE PROGRESÃO ARITMÉTICA",)
print("=-= "*8)
num=int(input("Informe o primeiro termo da P.A: "))
raz=int(input("Insira a razão de sua progresão: "))
enes=int(input("Digite o enésimo termo: "))
termo=num
cont=1

while cont<enes:
    print(f"{termo} -> ", end="")
    termo+=raz
    cont+=1
print("FIM")


esc=int(input("Deseja mostrar mais termos?\n[1] SIM\n[2] NÃO\nSua escolha: "))
while esc not in range(1,3):
    print("Opção inválida. Tente novamente")
    esc=int(input("\nDeseja mostrar mais termos?\n[1] SIM\n[2] NÃO\nSua escolha: "))

while esc!=2:
    nt=int(input("Quantos termos a mais deseja que seja mostrado: "))
    enes+=nt
    while cont<enes:
        print(f"{termo}", end="")
        termo+=raz
        cont+=1

print("Obrigado por usar nosso programa!")
