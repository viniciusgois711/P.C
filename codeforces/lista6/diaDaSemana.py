def dia_da_semana(h, d):
    l = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    x = 0
    while h != l[x]:
        x+=1
    return l[(x+d)%7]

