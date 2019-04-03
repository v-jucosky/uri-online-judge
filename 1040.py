notas = input().split(" ")

media = (2 * float(notas[0]) + 3 * float(notas[1]) + 4 * float(notas[2]) + float(notas[3])) / 10

print("Media: %.1f" % media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    media = (media + exame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media) 
