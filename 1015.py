n = 2

x = []
y = []
distancia = []

for i in range(n):
    posicao = input().split(" ")
    x.append(float(posicao[0]))
    y.append(float(posicao[1]))
    if i % 2 == 1:
        distancia.append(((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** (1/2))
        print("%.4f" % distancia[i // 2])
