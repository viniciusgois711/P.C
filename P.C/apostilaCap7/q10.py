def conta_digito(n,d):
    if n == 0:
        return 0
    if n%10==d:
        return 1+conta_digito(n//10,d)
    else:
        return 0+conta_digito(n//10,d)
    
numero = int(input())

print("0:",conta_digito(numero,0))
print("1:",conta_digito(numero,1))
print("2:",conta_digito(numero,2))
print("3:",conta_digito(numero,3))
print("4:",conta_digito(numero,4))
print("5:",conta_digito(numero,5))
print("6:",conta_digito(numero,6))
print("7:",conta_digito(numero,7))
print("8:",conta_digito(numero,8))
print("9:",conta_digito(numero,9))