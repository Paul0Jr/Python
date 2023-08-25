'''Crie um programa que leia dois valores e mostre um menu na tela.
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

while True:
    num=input(f"Digite o primeiro valor: ")
    num1=input(f"Digite o segundo valor: ")
    if num.isnumeric() and num1.isnumeric():
        num=int(num)
        num1=int(num1)
        print("")
        break
    else:
        print("Digite apenas números!")

while True:
    print(f"Você escolheu os números {num} e {num1}!")
    choice=input("\nQual operação deseja realizar?\n[1] Adição\n[2] Subtração\n[3] Multiplação\n[4] Divisão\n[5] Novos números\n[6] Sair do Programa\nSua escolha: ")[0]
    if choice.isnumeric():
        choice=int(choice)
        if choice in range(1,6):
            if choice==1:
                print(f"\nA soma entre {num} e {num1} é: {num+num1}\n")
                print("=-="*20)
                sleep(2)
                continue
            elif choice==2:
                if num>=num1:
                    print(f"\nA subtração entre {num} e {num1} é: {num-num1}")
                    print("=-="*20)
                    sleep(2)
                    continue
                elif num<num1:
                    print(f"\nA subtração de forma negativa entre {num} - {num1} = {num-num1}")
                    print(f"\nA subtração da forma positiva entre {num1} - {num} = {num1-num}")
                    print("=-="*20)
                    sleep(2)
                    continue
            elif choice==3:
                print(f"\nA multiplicação entre {num} x {num1} = {num*num1}")
                print("=-="*20)
                sleep(2)
                continue
            elif choice==4:
                if num>=num1:
                    print(f"A divisão entre {num} / {num1} = {num/num1}")
                    print("=-="*20)
                    sleep(2)
                    continue
                elif num<num1:
                    print(f"A divisão de forma negativa entre {num} / {num1} = {num/num1}")
                    print(f"A divisão de forma positiva entre {num1} / {num} = {num1/num}")
                    print("=-="*20)
                    sleep(2)
                    continue
            elif choice==5:
                num=input(f"\nDigite o primeiro valor: ")
                num1=input(f"Digite o segundo valor: ")
                if num.isnumeric() and num1.isnumeric():
                    num=int(num)
                    num1=int(num1)
                    print("=-="*20)
                    continue
                else:
                    print("Digite apenas números!")
            elif choice==6:
                print("Obrigado por usar nosso programa :)")
                sleep(2)
                break
        else:
            print("\nResponda apenas com o número da categoria que deseja utilizar!")
    else:
        print("\n1Responda apenas com o número da categoria que deseja utilizar!")