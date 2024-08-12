r = []

while True:
    h1, m1, h2, m2 = map(int,input().split())
    if (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0):
        break
    m = 0
    if h2>h1 or (h1==h2 and m1<m2):
        m = (h2-h1)*60 - (m1-m2)

    else:
        m = (24-(h1-h2))*60 - (m1-m2)

    r.append(m)

for x in range(0, len(r)):
    print(r[x])