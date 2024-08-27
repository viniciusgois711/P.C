qtdEntradas = int(input())
lEntrada = []
lRepetidos = []
novaLista = []
ultimo = -1
for x in range(0, qtdEntradas):
    digitado = int(input())
    if digitado in lEntrada:
        lRepetidos.append(digitado)
    lEntrada.append(digitado)
    ultimo = digitado

for x in lEntrada:
    if x in lRepetidos:
        novaLista.append(x)

print(lEntrada, lRepetidos)
print(novaLista)

