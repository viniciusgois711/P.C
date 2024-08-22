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
        print('nenhum')
    else:
        print(maiorX, menorY, menorU, maiorV)

