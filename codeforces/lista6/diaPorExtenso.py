def dia(dia, mes, ano):

    if mes>12 or dia>31:
        return "Data Invalida"
    if mes == 2 and dia > 28:
        return "Data Invalida"
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia >30:
        return "Data Invalida"
    
    l = ["janeiro", 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    if dia<10:
        dia = "0" + str(dia)
    retorno = str(dia) + " de " + str(l[mes-1]) + " de " + str(ano)
    return retorno

    


x, y, z = map(int, input().split("/"))

print(dia(x,y,z))