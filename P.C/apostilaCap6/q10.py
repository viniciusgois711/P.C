l = list(map(int,input().split()))

if sum(l)%len(l) == 0:
    print('Sim')
else: print('Nao')