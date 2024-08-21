qtd = int(input())
l= []
soma = vezes = 0

for x in range(0, qtd):
    y = int(input())
    l.append(y)
    soma += y

media = soma//qtd

for x in range(0,qtd):
    if l[x]>int(media*1.1) or l[x]<int(media*0.9):
        vezes += 1

print(media)
print(vezes)