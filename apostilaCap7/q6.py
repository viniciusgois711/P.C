def area(l,p):
    return l*p

def maior_2(x,y):
    if x>=y:
        return x
    else: return y

def maior_4(x,y,z,w):
    a = maior_2(x,y)
    b = maior_2(z,w)
    return maior_2(a,b)

def resultado(x):
    if x==areaA:
        return "A"
    elif x==areaB:
        return "B"
    elif x==areaC:
        return "C"
    else: return "D"
    
al, ap = map(int,input().split())
bl, bp = map(int,input().split())
cl, cp = map(int,input().split())
dl, dp = map(int,input().split())

areaA = area(al,ap)
areaB = area(bl,bp)
areaC = area(cl,cp)
areaD = area(dl,dp)

maior_area = maior_4(areaA, areaB, areaC, areaD)

print(resultado(maior_area))