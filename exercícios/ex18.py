'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math

angulo=float(input("Insira o valor do ângulo: "))

print("O seno, cosseno e tangente de {:.0f} serão, respectivamente {:.1f}, {:.1f} e {:.1f}".format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))