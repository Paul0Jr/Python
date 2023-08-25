'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

import math

num=float(input("Digite algum número real: "))

print("O número {} tem parte inteira sendo {}!".format(num, math.trunc(num)))