r = []
while True:
    x = int(input())
    if x == 0:
        break
    l = list(map(int,input().split()))
    m = []
    cont = 1
    l.append(l[0])
    l.append(l[1])
    if l[0]>l[1]:
        m.append(True)
    else:
        m.append(False)
 
    for i in range(1, len(l)):
        if l[i]>l[i-1]:
            m.append(True)
        else: m.append(False)
 
    for i in range(1, len(m)):
        if m[i] != m[i-1]:
            cont += 1
    cont = cont - 2
 
    r.append(cont)
 
for i in range(0, len(r)):
    print(r[i])