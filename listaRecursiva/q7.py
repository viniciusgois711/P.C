
def divisores_r(n,k):
    if k==1:
        return [1]
    
    l = divisores_r(n,k-1)

    if n%k==0:
        l.append(k)

    return l


def divisores(n):

    return divisores_r(n,n)

print(divisores(10))