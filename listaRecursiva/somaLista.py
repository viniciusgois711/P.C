def soma_r(l):
    qtd = len(l)

    if qtd == 0:
        return 0
    
    ultimo = l[qtd-1]

    nova_lista = l[:-1]
    soma_sublista = soma_r(nova_lista)
    return ultimo + soma_sublista



l = [1,2,3,4,5]
print(soma_r(l))