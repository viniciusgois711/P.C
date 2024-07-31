l = list(map(int,input().split()))

l[0], l[7] = l[7], l[0]

print(*l)