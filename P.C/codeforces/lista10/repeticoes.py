dna = input()
tamanho = 0
ultimo = ''
l = []

for x in range(0,len(dna)):
    if dna[x] != ultimo:
        l.append(tamanho)
        tamanho = 1
    else:
        tamanho += 1
    
    ultimo = dna[x]

l.append(tamanho)
l.sort(reverse=True)
print(l[0])