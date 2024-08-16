n, r = map(int,input().split())
l = list(map(int,input().split()))
nl = []

for x in range(1,n+1):
    if x not in l:
        nl.append(x)

if len(nl) == 0:
    print('*')
else:
    print(*nl, end=' ')
