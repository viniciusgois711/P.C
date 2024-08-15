
def func():
    copiaL = l.copy()
    ln = ''

    for x in range(0, qtd):
        m=0
        for i in range(0,len(l)):
            if l[i]>m:
                m = l[i]
            else:
                m = m

        if str(copiaL.index(m)) in ln:
            for x in range(len(copiaL)-1,0-1,-1):
                if m == copiaL[x]:
                    k = x
                    break
            ln += (str(k))
        else:
            ln += (str(copiaL.index(m)))
        l.remove(m)
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

