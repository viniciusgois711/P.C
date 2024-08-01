qtd = int(input())
l = []
ult = soma = 0
for x in range(1,qtd+1):
    n = int(input())
    l.append(n)

for x in range(0, qtd):
    if ult!=l[x]:
        ult = l[x]
        soma +=1

print(soma)