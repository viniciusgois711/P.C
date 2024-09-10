qtdEntrada = int(input())
entrada = []
c = []

for x in range(0, qtdEntrada):
    digitado = int(input())
    entrada.append(digitado)

if qtdEntrada>2:
    for x in range(0, qtdEntrada-1):

        for y in range(x+1, qtdEntrada):
            primeiro = entrada[x]
            segundo = entrada[y]

            ultimo = segundo
            if 

            for z in range(y+1, qtdEntrada):
                if entrada[z] == primeiro and entrada[z] != segundo:
                    t = primeiro
                    primeiro = segundo
                    segundo = t
                    contador += 1
            c.append(contador)
    print(max(c))
    print(c)
else:
    if qtdEntrada==1 or entrada[0] == entrada[1]:
        print(1)
    else:
        print(2)
