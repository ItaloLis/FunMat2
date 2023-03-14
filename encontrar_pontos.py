# Dados 2 pontos, calcular y=ax-b
# e decidir onde está um ponto P (=0, <0, > 0)

ponto1 = [3, 4]
ponto2 = [0, 6]
pontoP = [1, 2]

def sinal(x1, y1, x2, y2, x, y):
    a = (y2 - y1)/(x2 - x1)
    b = y1 - a*x1
    return y - a*x - b #mudar aq

x1 = 3
y1 = 4
x2 = 0
y2 = 6
xp = 1
yp = 2

print(round(sinal(x1, y1, x2, y2, xp, yp), 2))


# Verificar se um ponto P está dentro de um triângulo ABC
# Triângulo : x1, y1, x2, y2, x3, y3
# ponto P : x, y

def cadeop(x1, y1, x2, y2, x3, y3, x, y):
    local1 = sinal(x1, y1, x2, y2, x, y)
    local2 = sinal(x1, y1, x3, y3, x, y)
    local3 = sinal(x2, y2, x3, y3, x, y)

    if local1 * local2 * local3 == 0:
        return 'Dentro'
    elif [local1, local2, local3].count(-1) == 2:
        return 'Dentro'
    else:
        return 'Fora'


x1 = 1
y1 = 1
x2 = 0
y2 = 1
x3 = 3
y3 = 0
x = 0.5
y = 1.3

print(cadeop(x1, y1, x2, y2, x3, y3, x, y))
