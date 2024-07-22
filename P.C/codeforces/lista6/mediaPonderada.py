def media_ponderada(v1, p1, v2, p2):
    calculo = (v1*p1+v2*p2)/(p1+p2)

    return calculo


v1, v2 = map(int, input().split())
p1, p2 = map(int, input().split())

print(media_ponderada(v1,p1,v2,p2))