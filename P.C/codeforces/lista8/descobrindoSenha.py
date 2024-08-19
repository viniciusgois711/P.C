
def func():
    ln = ''

    for x in range(0, qtd):
        m=0
        for i in range(0,len(l)):
            if l[i]>m:
                m = l[i]

            else:
                m = m

        ln += (str(l.index(m)))
        l[l.index(m)] = -1

    return ln
    
resultado = []
while True:
    try:
        qtd = int(input())
        l = list(map(float,input().split()))

        resultado.append(func())
    except EOFError:
        break
    
for x in range(0, len(resultado)):
    print("Caso {}: {}".format(x+1, resultado[x]))
