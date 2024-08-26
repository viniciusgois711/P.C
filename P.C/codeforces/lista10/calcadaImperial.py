n = int(input())
entrada = []
for x in range(0, n):
    valor = int(input())
    entrada.append(valor)

l = []
nLista = []
lx = []
qtd = []

for x in range(0, n):
    vezes = 0    
    for i in range(0,n):
        if entrada[i] == x:
            vezes += 1

    if vezes > 1:
        l.append(x)
        qtd.append(vezes)

while len(l)>2:
    l.pop()

ultimo = ''
for x in range(0, n):
    if entrada[x] in l and ultimo != entrada[x]:
        nLista.append(entrada[x])
        ultimo = entrada[x]



for x in range(0, n):
    vezes = 0
    for i in range(0,len(nLista)):
        if nLista[i] == x:
            vezes +=1
        
    if vezes < 2:
        lx.append(x)



for x in range(0, len(lx)):
    if lx[x] in nLista:
        nLista.remove(lx[x])

resultado = 1
if len(nLista) < 2:
    print(resultado)
else:
    ultimo = nLista[0]
    for x in range(0, len(nLista)):

        if  ultimo != nLista[x]:
            resultado += 1

        ultimo = nLista[x]

    print(resultado)


print(nLista)

print(l)
print(qtd)