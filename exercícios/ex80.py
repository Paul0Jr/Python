'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()).
 No final, mostre a lista ordenada na tela.'''

lista=list()

for v in range(1,6):
    num=int(input(f"Digite o {v}° valor: "))
    if v==1 or num>lista[-1]:
        lista.append(num)
    else:
        posicao=0
        while posicao<len(lista):
            if num<=lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao+=1

print(f"Os valores digitados foram: \n{lista}") 