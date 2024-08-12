t = int(input())
maior = []

for z in range(0,t):
    d, n = map(int,input().split())
    m = list(map(float,input().split()))
    copia = m.copy()

    for x in range(0,n):
        while m[x]+copia[x]<=d:
            m[x] += copia[x]
    
    maior.append(0)
    for x in range(0,n):
        if d-m[x]>=maior[z]:
            maior[z] = d-m[x]
    
for x in range(0,t):
    print("{:.2f}".format(maior[x]))
            
