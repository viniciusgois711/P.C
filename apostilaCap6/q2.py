lista = list(map(int,input().split()))

a = lista[0]

lista[0] = lista[1]

lista[1] = a

print(*lista)