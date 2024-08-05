a = int(input())
b = int(input())
c = int(input())
d = int(input())

l = []

l.append(a)
l.append(b)
l.append(c)
l.append(d)

l.sort()

dupla1 = l[0] + l[3]
dupla2 = l[1] + l[2]

if dupla1>dupla2:
    print(dupla1-dupla2)
else:
    print(dupla2-dupla1)
