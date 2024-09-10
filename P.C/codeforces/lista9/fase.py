qtdCandidatos = int(input())
minimoAprovados = int(input())
listaCandidatos = []

aprovadosTotal = 0

for x in range(0, qtdCandidatos):
    candidato = int(input())
    listaCandidatos.append(candidato)

listaCandidatos.sort(reverse=True)

for x in range(0, minimoAprovados):
    aprovadosTotal += 1

verificador = aprovadosTotal

if verificador < qtdCandidatos:
    while listaCandidatos[verificador-1] == listaCandidatos[verificador]:
        aprovadosTotal += 1
        verificador += 1
        if verificador == qtdCandidatos:
            break

print(aprovadosTotal)