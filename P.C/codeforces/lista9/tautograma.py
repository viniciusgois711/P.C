resultado = []  
while True:
    l = list(map(str,input().upper().split()))
    ultimo = l[0][0]
    if ultimo == '*':
        break
    r = ''

    for x in range(len(l)-1, -1, -1):
        if ultimo == l[x][0]:
            r = 'Y'
        else:
            r = 'N'
            break
    resultado.append(r)

for x in range(0, len(resultado)):
    print(resultado[x])
