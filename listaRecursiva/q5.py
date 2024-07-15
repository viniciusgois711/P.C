def contaBin(n):
    if n == 1:
        return 1

    qtd = 1+contaBin(n//2)

    return qtd


print(contaBin(4312))