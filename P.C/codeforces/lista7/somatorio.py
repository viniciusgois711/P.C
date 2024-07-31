n = int(input())
soma = 0

for x in range(1, n+1):
    soma += 1/x

print("{:.4f}".format(soma))