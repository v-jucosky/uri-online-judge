entrada = input().split(" ")

item = int(entrada[0])
quantidade = int(entrada[1])

precos = [4.00, 4.50, 5.00, 2.00, 1.50]

print("Total: R$ %.2f" % (quantidade * precos[item - 1]))
