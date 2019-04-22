valor = input().split(".")
notas = int(valor[0])
moedas = int(valor[1])

notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = 0
moedas_100 = moedas_50 = moedas_25 = moedas_10 = moedas_5 = moedas_1 = 0

while notas - 100 >= 0:
    notas_100 += 1
    notas -= 100

while notas - 50 >= 0:
    notas_50 += 1
    notas -= 50

while notas - 20 >= 0:
    notas_20 += 1
    notas -= 20

while notas - 10 >= 0:
    notas_10 += 1
    notas -= 10

while notas - 5 >= 0:
    notas_5 += 1
    notas -= 5

while notas - 2 >= 0:
    notas_2 += 1
    notas -= 2

while notas - 1 >= 0:
    moedas_100 += 1
    notas -= 1

while moedas - 50 >= 0:
    moedas_50 += 1
    moedas -= 50

while moedas - 25 >= 0:
    moedas_25 += 1
    moedas -= 25

while moedas - 10 >= 0:
    moedas_10 += 1
    moedas -= 10

while moedas - 5 >= 0:
    moedas_5 += 1
    moedas -= 5

while moedas - 1 >= 0:
    moedas_1 += 1
    moedas -= 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % notas_100)
print("%d nota(s) de R$ 50.00" % notas_50)
print("%d nota(s) de R$ 20.00" % notas_20)
print("%d nota(s) de R$ 10.00" % notas_10)
print("%d nota(s) de R$ 5.00" % notas_5)
print("%d nota(s) de R$ 2.00" % notas_2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % moedas_100)
print("%d moeda(s) de R$ 0.50" % moedas_50)
print("%d moeda(s) de R$ 0.25" % moedas_25)
print("%d moeda(s) de R$ 0.10" % moedas_10)
print("%d moeda(s) de R$ 0.05" % moedas_5)
print("%d moeda(s) de R$ 0.01" % moedas_1)
