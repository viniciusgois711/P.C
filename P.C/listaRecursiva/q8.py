def indice(l):
    qtd = len(l)

    if qtd == 1:
        return 0
    
    nova_lista = l[:-1]
    elemento = indice(nova_lista)

    if l[elemento] > l[qtd-1]:
        return elemento
    else:
        return qtd-1


l = [7,8,10,3,2,1,9,12]
print(indice(l)) 