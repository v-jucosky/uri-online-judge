valores = input().split(" ")

for i in range(len(valores) - 1):
    maior = (int(valores[i]) + int(valores[i + 1]) + abs(int(valores[i]) - int(valores[i + 1]))) / 2
    valores[i + 1] = maior

print(valores[len(valores) - 1], "eh o maior")
