'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso=float(input("Insira seu peso em kg: "))
alt=float(input("Insira sua altura em metros: "))
imc=peso/(alt**2)
print("Seu imc é igual a {:.1f}".format(imc))
#DEFININDO O IMC
if imc<18.5:
    print("Você está abaixo do peso.")
elif 25>imc  and imc>=18.5:
    print("Peso ideal.")
elif 30>imc and imc>=25:
    print("Sobrepeso.")
elif 40>imc and imc>=30:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")