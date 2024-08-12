altPulo, canos = map(int,input().split())

altCano = list(map(int,input().split()))
ultimo = altCano[0]
somador = 0
for x in range(0, canos):

    if abs(altCano[x]-ultimo)<=altPulo:
        somador += 1
    
    ultimo = altCano[x]

if somador == canos:
    print('YOU WIN')
else:
    print('GAME OVER')
