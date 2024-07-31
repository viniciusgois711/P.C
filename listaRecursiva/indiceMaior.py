def indice(l):
    qtd = len(l)

    if qtd == 1:
        return 0
    
    nova_lista = l[:-1]

    x = indice(nova_lista)

    if l[qtd-1]>l[x]:
        return qtd-1
    else:
        return x
    

l = [1,2,5,4,4]

print(indice(l))