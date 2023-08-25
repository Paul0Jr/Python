'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase=str(input("Digite alguma frase aleatória: ")).strip().upper()
words=frase.split()
join=''.join(words)
inverso=''

for i in range(len(join) - 1, -1, -1):
    inverso+= join[i]
print(inverso)

if inverso==join:
    print(f"A frase '{frase}' é um palíndromo!")
else:
    print(f"A frase '{frase}' não é um palíndromo!")
