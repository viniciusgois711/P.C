import sys
sys.setrecursionlimit(100000)


def multiplos_r(num,limite, x):
    if x == 0:
        return []
    
    l = multiplos_r(num, limite, x-1)
    if x%num==0:
        l.append(x)

    return l
    
num, limite = map(int, input().split())
print(*multiplos_r(num, limite, limite))