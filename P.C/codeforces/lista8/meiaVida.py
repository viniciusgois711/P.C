tempo, massa = map(int,input().split())

t = 0
while massa>=0.5:
    massa = massa/2
    t += tempo

dias = t//86400
horas = (t%86400)//3600
minutos = ((t%86400)%3600)//60
segundos = (((t%86400)%3600)%60)

print('{} dias {:02d}:{:02d}:{:02d}'.format(dias,horas,minutos,segundos))