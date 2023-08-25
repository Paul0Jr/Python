'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase=input("Digite uma frase: ").strip().upper()

print("A letra 'A' aparece {} vezes.".format(frase.count('A')))
print("A letra 'A' aparece pela primeira vez na posição {}".format(frase.find('A')+1))
print("A letra 'A' aparece pela última vez na posição {}.".format(frase.rfind('A')+1))