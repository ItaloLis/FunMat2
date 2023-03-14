# Simulação de Monte Carlo
# Lançamento de dois dados p/ obter soma n

import random as rd

soma = 8
repeticoes = 10

cont = 0

for i in range(repeticoes): #joga os dados 8 vezes
    jogada = [rd.randint(1, 6) for k in range(2)] #sorteia um número de cada dado
    if jogada[0] + jogada[1] == soma:
        cont += 1

prob = 100*cont/repeticoes #Cálculo da probabilidade

print(prob)



#ou



def ndados(s, r):
    cont = 0
    for i in range(r):  # joga os dados 8 vezes
        jogada = [rd.randint(1, 6) for k in range(2)]  # sorteia um número de cada dado
        if jogada[0] + jogada[1] == s:
            cont += 1

    prob = round(100 * cont / r, 1)  # Cálculo da probabilidade / arredonda p uma casa decimal

    return prob

soma = 2
repeticoes = 10000

print([ndados(soma, repeticoes) for k in range(10)])
