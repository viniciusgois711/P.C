def conta_divisores_r(n,x):
    if x == 1:
        return 1
    if n%x==0:
        return 1+conta_divisores_r(n,x-1)
    else:
        return 0 + conta_divisores_r(n, x-1)
        

def conta_divisores(n):
    return conta_divisores_r(n,n)



print(conta_divisores(4))