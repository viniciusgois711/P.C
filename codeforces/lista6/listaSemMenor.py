def sublista_sem_menor(lista):
    menor = 1000
    for x in range(0, len(lista)):
        if lista[x] < menor:
            menor = lista[x]
    l = lista.copy()  
    lista.remove(menor)
    print(*l)
    print(*lista)



l = [2, 4, 6, 8, 1, 3, 5, 7]

print(sublista_sem_menor(l))