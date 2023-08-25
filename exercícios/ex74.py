'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
from time import sleep
tupla1=()
for i in range(0,5):
    pc=randint(0,10)
    tupla1+=(pc,)
print("Tupla gerada randomicamente")
sleep(0.5)
print(tupla1)
print(f"O maior valor da tupla {tupla1} é = {max(tupla1)}")
print(f"O menor valor da tupla {tupla1} é = {min(tupla1)}")