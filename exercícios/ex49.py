'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num=int(input("Escolha o número qual deseja visualizar a tabuada: "))

for i in range(1,11):
    print("{} x {} = {}".format(num, i, num*i))