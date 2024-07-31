def buscar_r(lista, x):
    qtd = len(lista)

    if qtd == 0:
        return -1
    
    ultimo = lista[qtd-1]
    nova_lista = lista[:-1]
    if ultimo == x:
        return qtd-1
    
    return buscar_r(nova_lista,x)


l = [1,8,3,4,5,6,7]

print(buscar_r(l,1))