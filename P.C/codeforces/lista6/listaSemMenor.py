def sublista_sem_menor(lista):
    menor = 10000000
    for x in range(0, len(lista)): 
        if lista[x] < menor:
            menor = lista[x]
    l = lista.copy()  
    l.remove(menor)
    
    return l



l = [2, 18, 18, 15, 17, 8, 14, 10, 12, 16]

print(sublista_sem_menor(l))