def conta_r(n):
    if n<10:
        return 1
    
    qtd = 1+conta_r(n/10)

    return qtd


print(conta_r(12345))