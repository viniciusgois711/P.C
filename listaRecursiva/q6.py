

def comb(n,k):
    
    if n==k:
        return 1
    if k == 1:
        return n

    result = comb(n-1,k-1) + comb(n-1,k)

    return result

print(comb(6,4))