a = input()
b = input()

copiaA = a
resultado = 0

for x in range(0, len(a)-len(b) + 1):
    vezes = 0
    for y in range(0, len(b)):
        if b[y] == copiaA[y]:
            break
        else:
            vezes += 1

    if vezes == len(b):
        resultado += 1
    copiaA = copiaA[1:]

print(resultado)
