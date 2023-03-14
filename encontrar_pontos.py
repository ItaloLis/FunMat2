# Dados 2 pontos, calcular y-ax-b
# e decidir onde está um ponto P (=0, <0, > 0)

ponto1 = [3, 4]
ponto2 = [0, 6]
pontoP = [1, 2]

def sinal(x1, y1, x2, y2, x, y):
    a = (y2 - y1)/(x2 - x1)
    b = y1 - a*x1
    return y - a*x - b

x1 = 3
y1 = 4
x2 = 0
y2 = 6
xp = 1
yp = 2

print(round(sinal(x1, y1, x2, y2, xp, yp), 2))
