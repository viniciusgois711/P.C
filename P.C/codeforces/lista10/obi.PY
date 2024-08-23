nCompetidores, pontosMinimos = map(int, input().split())
qtdAprovados = 0

for x in range(0, nCompetidores):
    nota1, nota2 = map(int,input().split())

    if nota1+nota2 >= pontosMinimos:
        qtdAprovados += 1

print(qtdAprovados)