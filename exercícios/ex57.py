'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

nome=str(input("Digite seu nome: ")).strip().title()
sexo=str(input("Digite seu sexo:\n(M) para Masculino \n(F) para feminino\nSua escolha: "))

while sexo not in 'MmFf':
    print("\nErro no reconhecimento do sexo. Por favor, digite novamente.")
    sexo1=str(input("Digite seu sexo:\n(M) para Masculino \n(F) para feminino\nSua escolha: "))
if sexo in 'Mm':
    sexo = 'masculino'
elif sexo in 'Ff':
    sexo = 'feminino'
print(f"\nSeu nome é {nome} e seu sexo é {sexo}!")