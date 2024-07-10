def lista_troca_menor_primeiro(lista):
    menor = 100
    indice = 0
    for x in range(0, len(lista)):
        if lista[x] < menor:
            menor = lista[x]
            indice = x
    
    l = lista.copy()
    l[indice] = l[0]
    l[0] = menor
    
    if l == lista:
        return 0, l
    return "1" + '!' + \
           l

lista = [2, 4, 6, 8, 1, 3, 5, 7]
print(lista_troca_menor_primeiro(lista))     
    # return 1, l

