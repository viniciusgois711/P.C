# def primo_r(n,x):
    
#     if x==1:
#         return 1

#     if n%x==0:
#         soma = 1 + primo_r(n,x-1)
    
#     else:
#         soma = 0 + primo_r(n,x-1)

#     return soma

# def primo(n):

#     verif = primo_r(n,n)

#     if verif > 2:
#         return "nao"

#     else:
#         return "sim"


# x = int(input())

# print(primo(x))

# Número primo
# n: [1,n] [2..n-1]

def primo_r(n, d):
    if d==1 or d==0:
        return True
    if n%d==0:
        return False
    else:
        return primo_r(n, d-1)

def primo(n):
    return primo_r(n, n-1)

x = int(input())
if (primo(x)):
    print("{:d} é primo!".format(x))
else:
    print("{:d} não é primo!".format(x))


