def ocorrencias(l,x):
    qtd = len(l)

    if qtd == 0:
        return 0
    
    nova_lista = l[:-1]

    if l[qtd-1] == x:
        return 1 + ocorrencias(nova_lista,x)
    else:
        return 0 + ocorrencias(nova_lista,x)
    

l = [1,2,3,3,3,3,4,2,5]

print(ocorrencias(l,3))