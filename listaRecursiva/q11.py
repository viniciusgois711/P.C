
def primo_r(n,k):
    if k == 1 or k == 0:
        return True
    if n%k==0:
        return False
    
    return primo_r(n,k-1)

def primo(n):

    return primo_r(n,n-1)

def primos(l):
    qtd = len(l)

    if qtd == 0:
        return []
    
    nova = l[:-1]

    l2 = primos(nova)

    if primo(l[qtd-1]) == True:
        l2.append(l[qtd-1])

    return l2

l = [9,7,6,3,2,1]

print(primos(l))
