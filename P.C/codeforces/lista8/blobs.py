qtd = int(input())
dias = []
for x in range(0, qtd):

    c = float(input())

    d = 0
    while c>1:
        d += 1
        c = c/2
    dias.append(d)
    
for x in range(0, len(dias)):
    print(dias[x], 'dias')
