y = 6
l = [-1, -1, 0, -1, -1, -1, 0, -1]

r = []
t = []
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
        if x >= 1:
            for w in range(x-1,l[0]-1,-1):
                if l[w]!=0:
                    soma2 += 1
                else:
                    soma2 += 1
                    break
        
        if soma1>9:
            soma1 = 9
        if soma2>9:
            soma2=9

        if soma1 == 0:
            soma1 = 10
        if soma2 == 0:
            soma2 = 10
        t.append(soma1)
        t.append(soma2)

        if soma1 == 0 or soma2<=soma1:
            r.append(soma2)
        elif soma2 == 0 or soma1<=soma2:
            r.append(soma1)

    else:
        r.append(0)

print(*r)
print(t)