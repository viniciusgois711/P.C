qtd = int(input())
l = list(map(int,input().split()))
menores = []
maiores = []
soma = eMenores = eMaiores = 0

for x in range(0, qtd):
    soma += l[x]

media = soma/qtd

for y in range(0, qtd):
    if l[y]>=media:
        eMaiores += 1
        maiores.append(l[y])

    elif l[y]<media:
        eMenores += 1
        menores.append(l[y])

print('{:.1f}'.format(media))
print(eMenores, end = ' ')
print(*menores)
print(eMaiores, end = ' ')
print(*maiores)