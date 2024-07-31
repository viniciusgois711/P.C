def tabuada_r(n, x):
    if x == 11:
        return 0
    
    print(x, ' x ', n, ' = ', n*x)

    return tabuada_r(n, x+1)

def tabuada(n):
    return tabuada_r(n, 1)


n = int(input())
tabuada(n)