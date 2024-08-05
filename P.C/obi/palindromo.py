qtd = int(input())
l = list(map(int,input().split()))

qtdLista = qtd-1

trocas = 0

for x in range(0, qtd//2):
    if l[x] != l[qtdLista-x]:
        trocas += 1

print(trocas)