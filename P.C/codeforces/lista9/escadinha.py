qtd = int(input())

l = list(map(int,input().split()))

r = 1

if len(l)>2:
    dif = l[1] - l[0]

    for x in range(1,len(l)):
        if l[x] - l[x-1] != dif:
            r+=1
        
        dif = l[x] - l[x-1]

print(r)