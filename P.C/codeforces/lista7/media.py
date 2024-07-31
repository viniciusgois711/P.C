qtd = int(input())
l = list(map(int,input().split()))

soma = menores = maiores = 0

for x in range(0, qtd):
    soma += l[x]

media = soma/qtd

for y in range(0, qtd):
    if l[y] < media:
        menores += 1
    else:
        maiores +=1

print('{:.1f}'.format(media))
print(menores)
print(maiores)