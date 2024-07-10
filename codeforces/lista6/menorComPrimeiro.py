def lista_troca_menor_primeiro(lista):
    menor = min(lista)
    indice = lista.index(menor)
    
    l = lista.copy()
    lista[indice] = lista[0]
    lista[0] = menor
    
    trocou = 1
    if l == lista:
        trocou = 0
    return trocou


l = [91, 58, -41, 85, -81, 87, 9, 10, -49, 39]

print(lista_troca_menor_primeiro(l))