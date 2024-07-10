def lista_troca_menor_primeiro(lista):
    menor = 100
    indice = 0
    for x in range(0, len(lista)):
        if lista[x] < menor:
            menor = lista[x]
            indice = x
    
    l = lista.copy()
    lista[indice] = lista[0]
    lista[0] = menor
    
    trocou = 1
    if l == lista:
        trocou = 0
    return trocou


l = [2, 4, 6, 8, 1, 3, 5, 7]

print(lista_troca_menor_primeiro(l))