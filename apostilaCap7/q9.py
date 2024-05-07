def exp(a,e):
    if e == 0:
        return 1
    
    return a*exp(a,e-1)

a,e = map(int,input().split())

print(exp(a,e))