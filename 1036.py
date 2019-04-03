valores = input().split(" ")

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (- B + delta ** (1/2)) / (2 * A)
    R2 = (- B - delta ** (1/2)) / (2 * A)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
