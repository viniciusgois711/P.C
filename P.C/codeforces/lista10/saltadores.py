l = list(map(int,input().split()))
r = []
for x in range(2,l[0]+1):
    r.append(abs(l[x]-l[x-1]))

r.sort()

for x in range(1, len(r)):
    if r[x] - r[x-1] != 1 or r[0] != 1 or r[len(r)-1] != l[0]-1:
        print('Nao alegre')
        break
    else:
        print('Alegre')
        break

print(r)