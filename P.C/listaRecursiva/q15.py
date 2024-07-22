def poli(coef,x):
    qtd = len(coef)
    if qtd == 0:
        return 0


    nova = coef[1:]
    result = coef[0]*x**(qtd-1) + poli(nova,x)

    return result

coef = [2,6,3,4,5]

x = 10

print(poli(coef,x))