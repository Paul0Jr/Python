'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''

matriz=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for c in range(0,3):
        matriz[i][c]=int(input(f"Digite um valor: "))

print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")