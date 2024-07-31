def ordenado(l):
    qtd = len(l)

    if qtd == 0:
        return True
    
    if l[qtd-1]<l[qtd-2]:
        return False
    
    nova = l[:-1]
    return ordenado(nova)

l = [1,3,2,5]

print(ordenado(l))