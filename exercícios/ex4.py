'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

test= input("Digite algo: ")

print("O tipo primitivo de '{}' é ".format(test), type(test))
print("Só tem espaços?", test.isspace())
print("É um número?", test.isnumeric())
print("É um título?", test.istitle())