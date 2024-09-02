final = []
while True:
    try:
        l = list(map(int,input().split()))
        r = []
        for x in range(2,l[0]+1):
            r.append(abs(l[x]-l[x-1]))

        r.sort()
        resultado = 'Alegre'
        if len(r) == 1 and r[0] != 1:
            resultado = 'Nao alegre'

        for x in range(1, len(r)):
            if r[x] - r[x-1] != 1 or r[0] != 1 or r[len(r)-1] != l[0]-1:
                resultado = 'Nao alegre'

        final.append(resultado)
            
    except EOFError:
        break

for x in range(0, len(final)):
    print(final[x])