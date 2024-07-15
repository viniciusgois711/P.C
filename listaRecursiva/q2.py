def primo_r(n,x):
    
    if x==1:
        return 1

    if n%x==0:
        soma = 1 + primo_r(n,x-1)
    
    else:
        soma = 0 + primo_r(n,x-1)

    return soma

def primo(n):

    verif = primo_r(n,n)

    if verif > 2:
        return "nao"

    else:
        return "sim"


x = int(input())

print(primo(x))