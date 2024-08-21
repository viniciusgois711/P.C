qtd = int(input())
l = list(map(int,input().split()))
a = b = 0

def testA(a):
    if a == 0:
        a = 1
    elif a == 1:
        a = 0

for x in range(0,len(l)):
    if l[x] == 1:
        if a == 0:
            a = 1
        elif a == 1:
            a = 0
    else:
        if b == 0:
            b = 1
        else:
            b = 0
        if a == 0:
            a = 1
        elif a == 1:
            a = 0

print(a)
print(b)