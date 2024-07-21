def junta(l1,l2):
    qtd1 = len(l1)
    qtd2 = len(l2)
    if qtd1==0:
        return l2
    if qtd2==0:
        return l1

    if l1[qtd1-1] > l2[qtd2-1]:
        nova = l1[:-1]
        l3 = junta(nova,l2)
        l3.append(l1[qtd1-1])
    
    else:
        nova = l2[:-1]
        l3 = junta(l1,nova)
        l3.append(l2[qtd2-1])


    return l3

l1 = [1, 3, 11, 13]
l2 = [2, 4, 10, 12]

print(junta(l1,l2))