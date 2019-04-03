N = int(input())
print(N)

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

while N - 100 >= 0:
    notas_100 += 1
    N -= 100

while N - 50 >= 0:
    notas_50 += 1
    N -= 50

while N - 20 >= 0:
    notas_20 += 1
    N -= 20

while N - 10 >= 0:
    notas_10 += 1
    N -= 10

while N - 5 >= 0:
    notas_5 += 1
    N -= 5

while N - 2 >= 0:
    notas_2 += 1
    N -= 2

while N - 1 >= 0:
    notas_1 += 1
    N -= 1

print("%d nota(s) de R$ 100,00" % notas_100)
print("%d nota(s) de R$ 50,00" % notas_50)
print("%d nota(s) de R$ 20,00" % notas_20)
print("%d nota(s) de R$ 10,00" % notas_10)
print("%d nota(s) de R$ 5,00" % notas_5)
print("%d nota(s) de R$ 2,00" % notas_2)
print("%d nota(s) de R$ 1,00" % notas_1)
