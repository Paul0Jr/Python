'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

tabelanome=()
tabelapreco=()
newtuple1=tabelanome
totalprice=0
while True:
    product=input("Digite o nome do produto: ").strip().capitalize()
    if product.isalpha():
        if len(product)<2:
            print("Escreva o nome completo do produto!\n")
            continue
        else:
            
            while True:
                price=input(f"\nDigite o preço de {product}:\nR$")
                if price.isnumeric():
                    price=int(price)
                    totalprice+=price
                    price=str(price)
                    newtuple1+=(product,price)
                    
                    break
                else:
                    print(f"Digite apenas o preço de {product}.\n")
    else:
        print("Por favor, digite apenas o nome do produto.\n")
    user_choice=input("\nDeseja continuar adicionar um produto? [S/N]\nSua escolha: ").upper()[0]
    if user_choice.isalpha():
        if user_choice=='N':
            break
        elif user_choice=='S':
            continue
    else:
        print("Responda apenas com S para 'Sim' e N para 'Não'!")

for pos in range(0, len(newtuple1)):
    if pos%2==0:
        print(f"{newtuple1[pos]:.<30}", end='')
    else:
        print(f"R${newtuple1[pos]}")