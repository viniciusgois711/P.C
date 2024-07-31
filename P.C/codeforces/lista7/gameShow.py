caixas = int(input())
l = []
saldo = 100
soma = maior = 0

for x in range(1, caixas+1):
    n = int(input())
    l.append(n)

for x in range(0, caixas):
    if maior>=sum(l):
        maior = maior
    else:
        maior = sum(l)

    l.pop()
    

print(100+maior)

