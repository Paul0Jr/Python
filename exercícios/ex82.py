'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
  Ao final, mostre o conteúdo das três listas geradas.'''

valores=[]
impar=[]
par=[]
while True:
  num=int(input("\nDigite um número: "))
  valores.append(num)
  # if num%2=0:
  #   valores.append(num)
  #   par.append(num)
  # else:
  #   valores.append(num)
  #   par.append(num)
  choice=str(input("\nDeseja continuar? S/N\nSua escolha: ")).upper()
  if choice not in "SN":
    print("Responda apenas com S para Sim e N para Não!")
    choice=str(input("Deseja continuar? S/N\nSua escolha: ")).upper()
  else:
    if choice=="N":
      break

for i, v in enumerate(valores):
  if v%2==0:
    par.append(v)
  elif v%2==1:
    impar.append(v)

print(f"\nA lista completa dos números digitados é: {valores}")
print(f"A lista contendo apenas números pares é: {par}")
print(f"A lista contendo apenas números ímpares é: {impar}")