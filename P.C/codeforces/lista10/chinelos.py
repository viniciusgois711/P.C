vendidos = 0
qtdTamanhos = int(input())
lista = []

for x in range(0, qtdTamanhos):
    qtdChinelos = int(input())
    lista.append(qtdChinelos)

qtdPedidos = int(input())

for x in range(0,qtdPedidos):
    escolhido = int(input())
    if lista[escolhido-1] >= 1:
        vendidos += 1
        lista[escolhido-1] -= 1

print(vendidos)