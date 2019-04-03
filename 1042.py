valores = input().split(" ")
originais = []

for i in range(len(valores)):
    originais.append(int(valores[i]))
    valores[i] = int(valores[i])

resultado = False
while resultado == False:
    j = 0
    k = 0
    resultado = True
    for j in range(len(valores) - 1):
        if valores[j] > valores[j + 1]:
            temp = valores[j]
            valores[j] = valores[j + 1]
            valores[j + 1] = temp
    for k in range(len(valores) - 1):
        if valores[k] > valores[k + 1]:
            resultado = False

for l in range(len(valores)):
    print(valores[l])

print()

for m in range(len(valores)):
    print(originais[m])
