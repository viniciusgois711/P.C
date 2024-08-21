j, r = map(int,input().split())
l = list(map(int,input().split()))

res = []
maior = 0
for y in range(0, j):
    res.append(0)
    for i in range(y,len(l),j):
        res[y] += l[i]
        
for x in range(len(res)-1, -1, -1):
    if res[x]>maior:
        maior = res[x]
        indice = x

print(indice+1)