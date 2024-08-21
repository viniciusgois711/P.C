l = []
while True: 
    n1, n2 = map(str,input().split())
    if n1 == '0' and n2 == '0':
        break

    somaA = int(n1)
    somaB = int(n2)

    while len(n1)>1:
        somaA = 0
        for x in range(0,len(n1)):
            somaA += int(n1[x])
        n1 = str(somaA)
    
    while len(n2)>1:
        somaB = 0
        for x in range(0,len(n2)):
            somaB += int(n2[x])
        n2 = str(somaB)

    if somaA>somaB:
        l.append(1)
    elif somaB>somaA:
        l.append(2)
    else:
        l.append(0)

for x in range(0,len(l)):
    print(l[x])
