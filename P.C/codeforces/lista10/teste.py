qtdEntrada = int(input())
entrada = []
r = []
contador = 1
c = []
for x in range(0, qtdEntrada):
    digitado = int(input())
    entrada.append(digitado)
if qtdEntrada>2:
    for x in range(0, qtdEntrada-1):
    while i < qtdEntrada-1:
        primeiro = entrada[x]

        for y in range(x+1, qtdEntrada):
            segundo = entrada[y]

            if primeiro != segundo:
                contador = 2
            else: 
                contador = 1

            for z in range(x+2, qtdEntrada):
                if entrada[z] == primeiro:
                    t = primeiro
                    primeiro = segundo
                    segundo = t
                    contador += 1
            c.append(contador)

print(c)
print(max(c))