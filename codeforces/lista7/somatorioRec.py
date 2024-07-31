import sys
sys.setrecursionlimit(1000000)

def somatorio_r(x):
    if x == 0:
        return 0
    
    soma = 1/x + somatorio_r(x-1)
    return soma

def formatar(x):
    if x == 0:
        return 0
    
    else:
        return format(x, '.4f')


x = int(input())
print(formatar(somatorio_r(x)))