def inverter(l):
    qtd = len(l)
    if qtd == 0:
        return []

    nova = l[1:]
    nova_r = inverter(nova)
    nova_r.append(l[0])

    return nova_r    

l = [1,2,3,4,5]

print(inverter(l))