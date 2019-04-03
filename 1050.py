DDD = [61, 71, 11, 21, 32, 19, 27, 31]
destino = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

entrada = int(input())
cadastro = 0

for i in range(len(DDD)):
    if DDD[i] == entrada:
        print(destino[i])
        cadastro = 1

if cadastro == 0:
    print("DDD nao cadastrado")
