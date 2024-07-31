l = list(map(int,input().split()))

x = len(l)

if x%2==0:
    elemento = (l[x//2 - 1] + l[x//2])/2
    print(elemento)
else:
    elemento = l[x//2]
    print(elemento)
