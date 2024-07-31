num, limite = map(int,input().split())

l = []
for x in range(num, limite+1):
    if x%num == 0:
        l.append(x)

print(*l)