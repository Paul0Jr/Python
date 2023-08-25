'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numbers=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    user=int(input("Digite um número entre 0 e 20: "))
    if 0<=user<=20:
        break
    else:
        print("Digite apenas um número entre 0 e 20!")

print(f"O número {user} por extenso é {numbers[user]}.")