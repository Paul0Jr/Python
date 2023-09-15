'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha. '''

maior=soma_par=terceira_coluna=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f"Digite um número a ser adicionado na linha {linha+1} coluna {coluna+1}: "))
        
# A) A soma de todos os valores pares digitados
        if matriz[linha][coluna]%2==0:
            soma_par+=matriz[linha][coluna]
# B) A soma dos valores da terceira coluna
        if matriz[linha][2]:
            terceira_coluna+=matriz[linha][2]
# C) O maior valor da segunda linha
        if matriz[1][coluna]:
            if matriz[1][coluna]==0:
                maior=matriz[1][coluna]
            else:
                if matriz[1][coluna]>maior:
                    maior=matriz[1][coluna]
    print("\n")

print(f"\nA matriz formatada:\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n")
print(f"A soma de todos os pares digitados = {soma_par}\n")
print(f"A soma dos elementos pertencentes apenas a terceira coluna = {terceira_coluna}\n")
print(f"O maior valor da segunda linha = {maior}\n")