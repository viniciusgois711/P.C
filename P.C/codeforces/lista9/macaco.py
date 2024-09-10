l = []
while True:
    qtd = int(input())
    if qtd == 0:
        break

    maiorX = maiorV = -100000
    menorY = menorU = 100000

    for x in range(0, qtd):
        x,y,u,v = map(int,input().split())

        if x >= maiorX:
            maiorX = x
        if y <= menorY:
            menorY = y
        if u <= menorU:
            menorU = u
        if v >= maiorV:
            maiorV = v

    if maiorX > menorU or menorY < maiorV:
        nova = []
        l.append(nova)
        nova.append('nenhum')
    else:
        nova = []
        l.append(nova)
        nova.append(maiorX)
        nova.append(menorY)
        nova.append(menorU)
        nova.append(maiorV)

for x in range(0, len(l)):
    print("Teste", x+1)
    print(*l[x])
    print()