n = int(input())

r = 'Sim'
if n>2:
    for x in range(2, n):
        if n%x == 0:
            r = 'Nao'
if n == 1:
    r = 'Nao'

print(r)