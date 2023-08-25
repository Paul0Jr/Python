'''Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num=0
soma=cont=media=maior=menor=0

while s in 'Ss':
    num=int(input("\nDigite um número: "))
    s=str(input("\nDeseja continuar digitando? [S/N]\nSua escolha: ")).upper()
    soma+=num
    cont+=1
    if cont==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        elif num<menor:
            menor=num

media=soma/cont
print("")
print(f"A média total entre os {cont} números digitados é de {media}!")
print(f"O maior valor digitado foi {maior}, enquanto o menor foi {menor}!")