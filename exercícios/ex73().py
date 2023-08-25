'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do usuário.'''

tabela=("Botafogo", "Flamengo", "Grêmio", "Fluminense", "Palmeiras", "Bragantino", "Fortaleza",
         "São Paulo", "Cruzeiro", "Internacional", "Athletico-PR", "Atlético-MG", "Santos", "Cuiabá",
           "Corinthians", "Bahia", "Goiás", "Coritiba", "Vasco da Gama", "América-MG")

user=input("Para qual time você torce? ").strip().title()
tabela+=(user,)

print(f"\nOs times do G5 são: ", end="")
print(" | ".join(tabela[0:5]))

print("\nOs times que estão na zona de rebaixamento são: ", end="")
print(" | ".join(tabela[16:20]))

print("\nOs times em ordenados de forma alfabética:")
print(" | ".join(sorted(tabela)))


print(f"\nO seu time está na {tabela.index(user)+1} posição")

