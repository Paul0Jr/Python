'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maiorpeso = 0
menorpeso = 0
for c in range(0, 5):
    peso = int(input('Digite seu peso: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if menorpeso == 0 or menorpeso > peso:
        menorpeso = peso

print(f'Considerando os valores informados, o maior peso foi: {maiorpeso} e o menor peso foi: {menorpeso}')