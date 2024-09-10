y = int(input())
l = list(map(int,input().split()))
r = []
for x in range(0,y):
    if l[x] != 0:
        soma1 = soma2 = 0
        if x<y:
            for z in range(x+1,y):
                if l[z]!=0:
                    soma1 += 1
                else:
                    soma1 += 1
                    break
                if z == y-1 and l[z] != 0:
                    soma1 = 10
        if x >= 1:
            for w in range(x-1,-1,-1):
                quebrou = False
                if l[w]==0:
                    soma2 += 1
                    quebrou = True
                    break
                else:
                    soma2 += 1
        if soma1>9 or soma1 == 0:
            soma1 = 9
        if soma2>9 or soma2 == 0 or not quebrou:
            soma2=9
        if soma1 == 0 or soma2<=soma1:
            r.append(soma2)
        elif soma2 == 0 or soma1<=soma2:
            r.append(soma1)
    else:
        r.append(0)
print(*r)
