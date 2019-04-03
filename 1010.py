total = 0

for i in range(2):
    entrada = input().split(" ")
    codigo_peca = int(entrada[0])
    numero_peca = int(entrada[1])
    valor_peca = float(entrada[2])
    total += valor_peca * numero_peca


print("VALOR A PAGAR: R$ %.2f" % total)
