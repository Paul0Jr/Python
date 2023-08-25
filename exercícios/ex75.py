'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
tupla=()
newtupla=tupla
pares=0
numpar=[]
impares=0
numimp=[]
for val in range(1,5):
    user=int(input(f"Digite o {val}° valor: "))
    newtupla+=(user,)
    if user%2==0:
        pares+=1
        numpar+=[user]
    else:
        impares+=1
        numimp+=[user]

print(f"\nO número 9 aparece {newtupla.count(9)} vezes." if newtupla.count(9)>0 else "\nO número 9 não foi digitado.")
print(f"\nO primeiro valor 3 foi digitado na {newtupla.index(3)+1}° posição." if newtupla.count(3)>0 else "\nO número 3 não foi digitado.")
print(f"\nUm total de {pares} números pares foi digitado, sendo eles: {numpar}" if pares>0 else "\nNenhum número par foi digitado.")
print(f"\nUm total de {impares} números ímpares foi digitado, sendo eles: {numimp}" if impares>0 else "\nNenhum número ímpar foi digitado.")