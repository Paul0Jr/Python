'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

import math
catop=float(input("Digite o valor do cateto oposto: "))
catad=float(input("Insira o valor do cateto adjacente: "))

print("O valor da hipotenusa será de: {:.1f}".format(math.hypot(catop, catad)))