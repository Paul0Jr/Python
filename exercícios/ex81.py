'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
A) Quantos números foram digitados; 
B) A lista de valores, ordenada de forma decrescente; 
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista=[]
while True:
    n=int(input("Digite algum número: "))
    lista.append(n)
    choice=str(input("Deseja continuar? S/N\nSua escolha: ")).upper()
    if choice not in "SN":
        print("Responda apenas com S para Sim e N para Não!")
        choice=str(input("Deseja continuar? S/N\nSua escolha: ")).upper()
    else:
        if choice=="N":
            break
    
print(f"\nA lista completa: {lista}")
print(f"Foram digitados um total de {len(lista)} números.\n")
lista.sort(reverse=True)
print(f"A lista ordenada de forma decrescente é: {lista}")
if 5 in lista:
    print(f"O valor 5 aparece na lista nas posições: {lista.index(5)}")
else:
    print("O valor 5 não foi digitado, logo não aparece na lista.")