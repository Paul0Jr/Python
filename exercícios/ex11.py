'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

altura=int(input("Insira a altura da parede em metros: "))
largura=int(input("Insira a largura da parede em metros: "))
area=altura*largura

print(f"Com uma área equivalente a {area}m², serão necessários um total de {area/2} litros de tinta para pintar a parede inteira!")