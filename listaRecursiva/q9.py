def soma(l):
    qtd = len(l)

    if qtd == 0:
        return 0
    
    nova = l[:-1]

    if l[qtd-1]%2==0:
        return l[qtd-1] + soma(nova)
    else:
        return 0 + soma(nova)
    

l = [2,4,3,8,10]

print(soma(l))